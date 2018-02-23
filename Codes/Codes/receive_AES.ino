// demo: CAN-BUS Shield, receive data with check mode
// send data coming to fast, such as less than 10ms, you can use this way
// loovee, 2014-6-13


#include <SPI.h>
#include "mcp_can.h"
#include <AESLib.h>

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 9;

MCP_CAN CAN(SPI_CS_PIN);                                    // Set CS pin

void setup()
{
    Serial.begin(115200);

    while (CAN_OK != CAN.begin(CAN_500KBPS))              // init can bus : baudrate = 500k
    {
        Serial.println("CAN BUS Shield init fail");
        Serial.println(" Init CAN BUS Shield again");
        delay(100);
    }
    Serial.println("CAN BUS Shield init ok!");

    
    
}

unsigned char buf1[8];
unsigned char buf2[8];
bool flag = true;
unsigned long time1,time2;

void loop()
{
    unsigned char len = 16;
    unsigned char buf[16];
    
    if(CAN_MSGAVAIL == CAN.checkReceive())            // check if data coming
    {
        if(flag){
          //buf = buf1;
          time1 = micros();
          CAN.readMsgBuf(&len, buf1);
        }else{
          CAN.readMsgBuf(&len, buf2);

          for(int i=0;i<16;i++){
            if(i<8) buf[i]=buf1[i];
            else buf[i]=buf2[i%8];
          }
          
         // buf = buf1+buf2;
          unsigned int canId = CAN.getCanId();  
        
      
          Serial.println("-----------------------------");
          Serial.print("Get data from ID: ");
          Serial.println(canId, HEX);
         for(int i=0;i<16;i++){
              Serial.print(buf[i],HEX);
            Serial.print(" ");
          }
          Serial.println("");
          uint8_t key[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
          aes128_dec_single(key, buf);
          Serial.print("decrypted:");
          //Serial.println(buf);
          for(int i=0;i<16;i++){
            Serial.print(buf[i],HEX);
            Serial.print(" ");
          }
          Serial.println("");

          time2 = micros();
          Serial.println((time2-time1));
/*          for(int i = 0; i<len; i++)    // print the data
          {
              Serial.print(buf[i], HEX);
              Serial.print("\t");
          }
          Serial.println();*/
        }
        flag = !flag;
    }
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/