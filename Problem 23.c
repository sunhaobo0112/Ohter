//
//  problem.c
//  problem 23
//
//  Created by SUN HAOBO on 16/6/8.
//  Copyright (c) 2016年 SUNHAOBO. All rights reserved.
//

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define RAND() ((double)rand()/((double)RAND_MAX+1.0))

int main(void)
{
    char d1,d2,d3='0';    //天気を表する変数day1,day2,day3を宣言する
    d1='H';    //day1は晴
    d2='K';    //day2は雲
    printf("6月1日の天気は晴\n");
    printf("6月2日の天気は雲\n");
    double lh=0.0,lk=0.0,la=0.0;   //18日目各天気の回数を宣言する
    double w;       //random生成の数を宣言する
    int i,j;        //循環過程で天数を表する数を宣言する
    srand((unsigned int)time(NULL)+i*10);     //random数を生成
   
    for(j=0;j<100000;j++){                //100000回18日の天気を求める
        for(i=3;i<=18;i++){               //3日目から18日まで循環,day1とday2の天気からday3の天気の確率を推測
            w=RAND();
            //printf("w=%f\n",w);
            //1日目晴、2日目は晴の場合、生成したrandom数の値により3日目の天気を推測する
            if(d1=='H' && d2=='H'){
                if(w<0.6){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.6 && w<0.9){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.9){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='H' && d2=='K'){
                if(w<0.2){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.2 && w<0.6){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.6){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='H' && d2=='A'){
                if(w<0.3){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.3 && w<0.7){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.7){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='K' && d2=='H'){
                if(w<0.7){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.7 && w<0.9){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.9){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='K' && d2=='K'){
                if(w<0.2){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.2 && w<0.8){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.8){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='K' && d2=='A'){
                if(w<0.1){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.1 && w<0.3){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.3){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='A' && d2=='H'){
                if(w<0.3){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.3 && w<0.7){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.7){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='A' && d2=='K'){
                if(w<0.4){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.4 && w<0.8){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.8){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
            else if (d1=='A' && d2=='A'){
                if(w<0.1){
                    d3='H';
                    d1=d2;
                    d2=d3;
                }
                else if(w>=0.1 && w<0.4){
                    d3='K';
                    d1=d2;
                    d2=d3;
                }
                else if (w>=0.4){
                    d3='A';
                    d1=d2;
                    d2=d3;
                }
            }
        }
        //各天気の回数を加算する
        if(d3=='H'){
            lh=lh+1;       //18日は晴の場合lh+1
        }
        else if(d3=='K'){
            lk=lk+1;       //18日は雲の場合lk+1
        }
        else if(d3=='A'){
            la=la+1;       //18日は雨の場合la+1
        }
    }
    printf("シミュレーション法でもらった6月18日の天気の確率は\n　晴%.4f 雲%.4f 雨%.4f\n",lh/100000,lk/100000,la/100000);
    
    
    //理論値
    
    double sh1=0.2,sk1=0.4,sa1=0.4;
    double sh2,sk2,sa2,sh3=0.0,sk3=0.0,sa3=0.0;
    //4日目
    sh2=sh1*0.7+sk1*0.2+sa1*0.1;
    sk2=sh1*0.2+sk1*0.6+sa1*0.2;
    sa2=sh1*0.1+sk1*0.2+sa1*0.7;
    //5日目から18日目
    for(i=5;i<=18;i++){
        sh3=sh1*sh2*0.6+sh1*sk2*0.2+sh1*sa2*0.3+
            sk1*sh2*0.7+sk1*sk2*0.2+sk1*sa2*0.1+
            sa1*sh2*0.3+sa1*sk2*0.4+sa1*sa2*0.1;
        sk3=sh1*sh2*0.3+sh1*sk2*0.4+sh1*sa2*0.4+
            sk1*sh2*0.2+sk1*sk2*0.6+sk1*sa2*0.2+
            sa1*sh2*0.4+sa1*sk2*0.4+sa1*sa2*0.3;
        sa3=sh1*sh2*0.1+sh1*sk2*0.4+sh1*sa2*0.3+
            sk1*sh2*0.1+sk1*sk2*0.2+sk1*sa2*0.7+
            sa1*sh2*0.3+sa1*sk2*0.2+sa1*sa2*0.6;
        sh1=sh2;
        sk1=sk2;
        sa1=sa2;
        sh2=sh3;
        sk2=sk3;
        sa2=sa3;
    }

    
    printf("理論的に6月18日の天気の確率は\n　晴%.4f 雲%.4f 雨%.4f\n",sh3,sk3,sa3);
    
    return 0;
}