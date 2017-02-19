
#include <SoftwareSerial.h>

SoftwareSerial Sim900(6, 7);
unsigned short maxStringLength_ = 64;
String serialIn_;
boolean serialInComplete_ = false;
boolean sim900InComplete_ = false;
String sim900In_;
String time_;
String sender_;
void setup() {
  serialIn_.reserve(maxStringLength_);
  sim900In_.reserve(maxStringLength_);
  serialIn_ = "";
  sim900In_ = "";
  Sim900.begin(19200);
  Serial.begin(19200);
}

void loop() {
  if (serialInComplete_) {
    cleanString(serialIn_);
    Serial.println(serialIn_);
    if (serialIn_.startsWith("SMS:")) {
      Serial.println("sending sms");
      serialIn_ = serialIn_.substring(4);
      int index  = serialIn_.indexOf(";");
      if (index < 0) {
        done();
        return;
      }
      String number = serialIn_.substring(0, index);
      String text = serialIn_.substring(index + 1);
      Serial.print("number:");
      Serial.println(number);
      Serial.print("text:");
      Serial.println(text);
      //sendSMS(number, text);
    }
    else if (serialIn_.startsWith("AT")) {
      Serial.println("sending to sim900");
      Sim900.print(serialIn_ + "\r");
    }
    else {
      Serial.println("nothing");
    }
    done();
  }

  extractSimString();
  if (!sim900InComplete_)
    return;
  evaluateSimString();
  sim900InComplete_ = false;
  sim900In_ = "";

}

void evaluateSimString() {
  if (sim900In_.indexOf(F("+CMT:")) >= 0) { //SMS received
    evaluateIncomingSMS();
  }
  else{
    Serial.println(sim900In_);
  }
}

void extractSender() {
  short index = sim900In_.indexOf(",");
  sender_ = sim900In_.substring(7, index - 1);
}

short extractTime() {
  short index = sim900In_.indexOf(",");
  String remainder = sim900In_.substring(index + 1);
  index = remainder.indexOf(",");
  time_ =  remainder.substring(index + 1, remainder.length());
  return remainder.length();
}
void evaluateIncomingSMS() {
  extractSender();
  short index = extractTime();
  Serial.print("Time: ");
  Serial.println(time_);
  Serial.print("Sender: ");
  Serial.println(sender_);
  Serial.print("Text: ");
  String text = sim900In_;
  Serial.println(text);
  
}
void extractSimString() {
  while (Sim900.available() > 0)
  {
    char inChar = (char)Sim900.read();
    if (inChar == '\r') {
      cleanString(sim900In_);
      if (sim900In_.length() > 0) {
        sim900InComplete_ = true;
      }
      return;
    }
    sim900In_ += inChar;
  }
}
void cleanString(String &stringToClean) {
  stringToClean.replace("\n", "");
  stringToClean.replace("\r", "");
  stringToClean.trim();
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    if (inChar == '\r') {
      serialInComplete_ = true;
      return;
    }
    if (serialIn_.length() > maxStringLength_)
    {
      //Serial.println("size of input string to big. clipping message");
      serialInComplete_ = true;
      return;
    }
    serialIn_ += inChar;
  }

}



void done() {
  Serial.println(F("Done"));
  // clear the string:
  serialIn_ = "";
  serialInComplete_ = false;
}

void sendSMS(String number, String msg)
{
  Serial.println(F("sending SMS"));
  Serial.println(number);
  Serial.println(msg);
  delay(100);
  Sim900.print("AT+CMGF=1\r");
  delay(100);
  Sim900.println("AT+CMGS=\"" + number + "\"");
  delay(100);
  Sim900.println(msg);
  delay(100);
  Sim900.print((char)26);

}
