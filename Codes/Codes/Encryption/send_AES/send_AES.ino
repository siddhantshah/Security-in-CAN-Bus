// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>
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

unsigned char stmp[8] = {0, 1, 2, 3, 4, 5, 6, 7};//,1},2,3,4,5};
unsigned char data[16];
unsigned long time1,time2;
void loop()
{

    time1 = micros();
    Serial.println(time1);
    for(int i=0;i<16;i++){
      if(i>=8) data[i]=0;
      else{
        data[i]=(stmp[i]);
        Serial.print(data[i],HEX);
        Serial.print(" ");
      }
    }
    Serial.println();
     //Serial.print(data,HEX);
    uint8_t key[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    aes128_enc_single(key,data);
   
   Serial.print("encrypted:");
    for(int i=0;i<16;i++){
      Serial.print(data[i],HEX);
      Serial.print(" ");
    }
    Serial.println("");
    
   /* aes128_dec_single(key, data);
    Serial.print("decrypted:");
    //Serial.println(stmp);
    for(int i=0;i<8;i++){
      Serial.print(data[i],HEX);
      Serial.print(" ");
    }
    Serial.println("");
*/  
    unsigned char data1[8];
    unsigned char data2[8];
    for(int i=0;i<16;i++){
    if(i<8) data1[i]=data[i];
    else data2[i%8]=data[i];
      
    }
     
    // send data:  id = 0x00, standrad frame, data len = 8, stmp: data buf
    CAN.sendMsgBuf(0x00, 0, 8,  data1);
    CAN.sendMsgBuf(0x00, 0, 8,  data2);
    time2 = micros();
   Serial.println((time2-time1));
   //  Serial.println("");

    delay(100);                       // send data per 100ms
}

