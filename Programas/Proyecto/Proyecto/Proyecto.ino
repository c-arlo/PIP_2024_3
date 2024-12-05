#include <LiquidCrystal_I2C.h>
#include <SevSeg.h>
#include <IRremote.h>

SevSeg sevseg;
LiquidCrystal_I2C lcd(0x27, 20, 4);
int pot = A3;
int RECV_PIN = 13;

void setup() {
  lcd.init();
  Serial.begin(9600);
  Serial.setTimeout(10);
  lcd.backlight();
  lcd.print("Jukebox V1");

  byte numDigits = 4;
  byte digitPins[] = { 2, 3, 4, 5 };
  byte segmentPins[] = { 6, 7, 8, 9, 10, 11, 12, 13 };
  bool resistorsOnSegments = false;      // 'false' means resistors are on digit pins
  byte hardwareConfig = COMMON_CATHODE;  // See README.md for options
  bool updateWithDelays = false;         // Default 'false' is Recommended
  bool leadingZeros = true;              // Use 'true' if you'd like to keep the leading zeros
  bool disableDecPoint = false;          // Use 'true' if your decimal point doesn't exist or isn't connected

  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments,
               updateWithDelays, leadingZeros, disableDecPoint);
  sevseg.setBrightness(90);
  sevseg.setNumber(0, 2);

  IrReceiver.begin(RECV_PIN, DISABLE_LED_FEEDBACK);
}

String msg, input, m;
unsigned long timer;
int secs = 0;
int mins = 0;
bool pause = true;
int pos = 0;
int valor;
int pvalor = -1;

void loop() {
  valor = analogRead(pot);
  valor = map(valor, 0, 1024, 0, 100);
  if (valor != pvalor) {
    Serial.println("V/"+String(valor));
    pvalor = valor;
  }

  if (IrReceiver.decode()) {
    m = IrReceiver.decodedIRData.decodedRawData, HEX;
    //Serial.println(m);
    if (m == "3125149440") {
      Serial.println("T/STOP");
    } else if(m == "3141861120") {
      Serial.println("T/PLAY");
    } else if(m == "3208707840") {
      Serial.println("T/PREV");
    } else if(m == "3158572800") {
      Serial.println("T/NEXT");
    } else if(m == "3860463360") {
      Serial.println("T/REWIND");
    } else if(m == "3091726080") {
      Serial.println("T/MUTE");
    } else if(m == "4127850240") {
      Serial.println("T/VOLUP");
    } else if(m == "3927310080") {
      Serial.println("T/VOLDOWN");
    }
    IrReceiver.resume();
  }

  if (Serial.available() > 0) {
    input = Serial.readString();
    if (input.substring(0, 2) == "T/") {
      if (input.substring(2) == "PAUSE") {
        pause = true;
      } else if (input.substring(2) == "PLAY") {
        pause = false;
      } else if (input.substring(2) == "REWIND") {
        pause = true;
        sevseg.setNumber(0);
        secs = -1;
        mins = 0;
        timer = 0;
      } else if (input.substring(2) == "STOP") {
        lcd.clear();
        lcd.print("Jukebox V1");
        pause = true;
        sevseg.setNumber(0, 2);
        secs = -1;
        mins = 0;
        timer = 0;
      }

    } else if (input.substring(0, 2) == "M/") {
      lcd.clear();
      msg = input.substring(2);
      lcd.print(msg);
      pos = 16;
    }
  }

  if (!pause) {
    if (millis() - timer >= 1000) {
      lcd.scrollDisplayLeft();
      timer = millis();
      pos++;
      if (pos > msg.length() + 1) {
        pos = 16;
        lcd.home();
      }
      secs++;
      if (secs == 60) {
        pos++;
        secs = 0;
        mins++;
      }
      sevseg.setNumber((mins * 100 + secs), 2);
    }
  }
  sevseg.refreshDisplay();
}