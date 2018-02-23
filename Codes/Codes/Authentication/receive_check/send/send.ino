// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>
#include "sha1.h"

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

unsigned char stmp[8] = {0, 1, 2, 3, 4, 5, 6, 7};
unsigned long nonce = 300;

void loop()
{
    char stmp1[8] = {0, 1, 2, 3, 4, 5, 6, 7};
    uint8_t *hash;
    //string s;
    for(int i=0;i<8;i++){
      //key
    }
    Sha1.initHmac(nonce+stmp,16); // key, and length of key in bytes
    Sha1.print(stmp1);
Serial.println("-----------------------------");
    Serial.print("Data Sent: ");
    for(int i = 0; i<8; i++)    // print the data
    {
        Serial.print(stmp[i], HEX);
        Serial.print("\t");
    }
    Serial.println();

    
    Serial.print("Hashed Data: ");
    hash = Sha1.resultHmac();
    for(int i=0;i<20;i++){
      Serial.print(hash[i]);  
    }
    Serial.println("");
    

//    uint8_t *hash;
////  Sha1.initHmac("hash key",8); // key, and length of key in bytes
//  Sha1.print("This is a message to hash");
 // hash = Sha1.resultHmac();

    
    // send data:  id = 0x00, standrad frame, data len = 8, stmp: data buf
    CAN.sendMsgBuf(0x10000, 1, 8, stmp);
    delay(1000);                       // send data per 100ms
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
