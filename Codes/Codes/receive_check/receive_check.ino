// demo: CAN-BUS Shield, receive data with check mode
// send data coming to fast, such as less than 10ms, you can use this way
// loovee, 2014-6-13


#include <SPI.h>
#include "mcp_can.h"
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

unsigned long nonce = 300;
bool flag = false;

void loop()
{
    unsigned char len = 0;
    unsigned char buf[8];

    if(CAN_MSGAVAIL == CAN.checkReceive())            // check if data coming
    {
        
        CAN.readMsgBuf(&len, buf);    // read data,  len: data length, buf: data buf

        if(flag){
          nonce=0;
          for(int i=0;i<8;i++){
            nonce = nonce+buf[i];
          }
          flag = false;
        }

        char buf1[8];
        for(int i=0;i<8;i++){
          buf1[i] = buf[i];
        }
        uint8_t *hash;
        Sha1.initHmac("key",3); // key, and length of key in bytes
        Sha1.print(buf1);
        hash = Sha1.resultHmac();
        for(int i=0;i<20;i++){
          Serial.print(hash[i]);  
        }
        Serial.println("");
        unsigned int canId = CAN.getCanId();
        uint8_t *rcvd_hash;
        
        Serial.println("-----------------------------");
        Serial.print("Get data from ID: ");
        Serial.println(canId, HEX);

        for(int i = 0; i<len; i++)    // print the data
        {
            Serial.print(buf[i], HEX);
            Serial.print("\t");
        }
        Serial.println();

        nonce = nonce+1;
    }
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
