package com.example.lopasgatlo;

import android.graphics.Color;
import android.hardware.*;
import android.os.*;
import android.view.*;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private SensorManager sm;
    private View layout;
    private TextView tv;
    private EditText pin;
    private Button btnArm, btnDisarm;

    private boolean armed, ringing, isRed;
    private final Handler h = new Handler();
    private Runnable flash;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        layout = findViewById(R.id.mainLayout);
        tv = findViewById(R.id.tvStatus);
        btnArm = findViewById(R.id.btnArm);
        pin = findViewById(R.id.etPin);
        btnDisarm = findViewById(R.id.btnDisarm);
        sm = (SensorManager) getSystemService(SENSOR_SERVICE);

        // Villogás logika lambda kifejezéssel és ternáris operátorral
        flash = () -> {
            layout.setBackgroundColor((isRed = !isRed) ? Color.RED : Color.WHITE);
            h.postDelayed(flash, 200);
        };

        // Élesítés logika beágyazva
        btnArm.setOnClickListener(v -> {
            btnArm.setEnabled(false);
            new CountDownTimer(5000, 1000) {
                public void onTick(long m) { tv.setText("Élesítés: " + m / 1000 + " mp"); }
                public void onFinish() {
                    armed = true;
                    tv.setText("ÉLESÍTVE!\nNe mozdítsd meg!");
                    btnArm.setVisibility(View.GONE);
                }
            }.start();
        });

        // Leállítás logika beágyazva
        btnDisarm.setOnClickListener(v -> {
            if ("1234".equals(pin.getText().toString())) {
                ringing = false;
                h.removeCallbacks(flash);
                layout.setBackgroundColor(Color.WHITE);
                tv.setText("Készen áll");
                pin.setText("");
                pin.setVisibility(View.GONE);
                btnDisarm.setVisibility(View.GONE);
                btnArm.setVisibility(View.VISIBLE);
                btnArm.setEnabled(true);
                Toast.makeText(this, "Riasztó leállítva.", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(this, "Hibás PIN kód!", Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public void onSensorChanged(SensorEvent e) {
        // Gyorsulás ellenőrzése egyetlen if-ben
        if (armed && !ringing && Math.abs(Math.sqrt(e.values[0]*e.values[0] + e.values[1]*e.values[1] + e.values[2]*e.values[2]) - SensorManager.GRAVITY_EARTH) > 2.0f) {
            ringing = true;
            armed = false;
            tv.setText("RIASZTÁS!!!");
            pin.setVisibility(View.VISIBLE);
            btnDisarm.setVisibility(View.VISIBLE);
            h.post(flash);
        }
    }

    @Override public void onAccuracyChanged(Sensor s, int a) {}

    @Override
    protected void onResume() {
        super.onResume();
        if (sm != null) sm.registerListener(this, sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER), SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (sm != null) sm.unregisterListener(this);
        h.removeCallbacks(flash);
        layout.setBackgroundColor(Color.WHITE);
    }
}