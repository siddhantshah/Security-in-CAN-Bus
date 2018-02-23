// demo: CAN-BUS Shield, receive data with check mode
// send data coming to fast, such as less than 10ms, you can use this way
// loovee, 2014-6-13


#include <SPI.h>
#include "mcp_can.h"
#include "sha1.h"
#include "Mechanic.h"

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
   // CAN.init_Mask(0,1, 0);            /* init Masks                   */
    //CAN.init_Filt(0, 1, 0);               /* init filters  */

        CAN.init_Mask(0, 0, 0x3ff);                         // there are 2 mask in mcp2515, you need to set both of them
    CAN.init_Mask(1, 0, 0x3ff);


    /*
     * set filter, we can receive id from 0x04 ~ 0x09
     */
    CAN.init_Filt(0, 0, 0x04);                          // there are 6 filter in mcp2515
    CAN.init_Filt(1, 0, 0x05);                          // there are 6 filter in mcp2515

    CAN.init_Filt(2, 0, 0x06);                          // there are 6 filter in mcp2515
    CAN.init_Filt(3, 0, 0x07);                          // there are 6 filter in mcp2515
    CAN.init_Filt(4, 0, 0x08);                          // there are 6 filter in mcp2515
    CAN.init_Filt(5, 0, 0x09);                          // there are 6 filter in mcp2515
    Serial.println("CAN BUS Shield init ok!");
}

void loop()
{
  
    unsigned char len = 0;
    unsigned char buf[8];

    if(CAN_MSGAVAIL == CAN.checkReceive())            // check if data coming
    {
        
        CAN.readMsgBuf(&len, buf);    // read data,  len: data length, buf: data buf

        unsigned long canId = CAN.getCanId();
        if(CAN.isExtendedFrame()) {

          for(int i=0;i<-1;i++)
          Serial.println("-----------------------------");
        }
        
        Serial.println("-----------------------------");
        Serial.print("Get data from ID: ");
        Serial.println(canId, HEX);
       
        for(int i = 0; i<len; i++)    // print the data
        {
            Serial.print(buf[i], HEX);
            Serial.print("\t");
        }
        Serial.println();

    }
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
