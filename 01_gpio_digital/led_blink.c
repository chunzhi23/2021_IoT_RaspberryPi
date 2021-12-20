#include <wiringPi.h>
#define LED_PIN 7

int main(){
    wiringPiSetup();
    pinMode(LED_PIN, OUTPUT);
    for (int i = 0 ; i < 5; i++){
        digitalWrite(LED_PIN, HIGH); delay(1000);   //HIGH or 1
        digitalWrite(LED_PIN,  LOW); delay(1000);   //LOW  or 0
    }

    return 0;
}