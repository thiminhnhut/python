
    /**
    * @brief  Function tinh chi so Humindex
    *
    *         Cong thuc tinh: Humindex = T + 5/9 * (e - 10)
    *
    *         Trong do: e = 6.112 * 10^(7.5 * T/(237.7 + T))*H/100
    *
    *
    * @param  T nhiet do  (do C)
    * @param  H do am  (%) (kieu float)
    *
    * @return
    *    - Chi so humidex
     */

#include <math.h>
float HumIndex(float T, float H){

    float e = 6.112*powf(10.0, 7.5*T/(237.7 + T))*H/100.0;
    float hindex = T + 5.0/9.0*(e - 10.0);
    return hindex;
}

float HumIndex2(float T, float H){

    float e = 6.112*powf(10.0, 7.5*T/(237.7 + T))*H/100.0;
    float hindex = T + 5.0/9.0*(e - 10.0);
    return hindex;
}

/* Example
//=============================================

#include <Arduino.h>
#include "../../libraries/humindex/humindex.h"

void setup(){
    Serial.begin(9600);
    float T = 32.0, H = 70.0;
    float e = HumIndex(T, H);
    Serial.println(e);
}

void loop(){
    ;
}

//=============================================
*/
