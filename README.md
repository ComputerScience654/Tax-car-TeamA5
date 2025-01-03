# โปรแกรมคำนวณภาษีรถยนต์ 4 ประตู
เป็นการคำนวณภาษีตามขนาดของเครื่องยนต์ (CC) และสามารถลดหย่อนภาษีได้เมื่ออายุของรถ มีอายุตั้งแต่ 6-10 ปี โดย 6 ปี จะลด10% ไปจนถึง 10 ปี ลด 50%

## หัวข้อ
[ผลลัพธ์](#ผลลัพธ์) | 
[การทำงานของโปรแกรม](#การทำงานของโปรแกรม) | 
[FlowChart](#flowchart) | 
[สมาชิก](#สมาชิก) 


## ผลลัพธ์
แบบที่ 1 ``` ลดหย่อนภาษี ```

![image](https://github.com/user-attachments/assets/32e47ffd-c794-4aff-b4d7-1bb55e0e70e6)

* ในภาพเป็นการลดหย่อนภาษี 10 % เนื่องจากรถมีอายุ 6 ปี

แบบที่ 2 ``` แบบปกติ ```

![image](https://github.com/user-attachments/assets/67e18b23-a8a9-439d-8b5c-ee14aa9c7543)

* ในภาพเป็นการเสียภาษีแบบปกติ

## การทำงานของโปรแกรม

1.แสดงตัวเลือก ของขนาด```เครื่องยนต์ (CC) โดยกำหนดค่าให้```  ``` Choice 1 = 1200  ```, ``` 2 = 1900  ```, ``` 3 = 2000  ```, ``` 4 = 3000  ```

![image](https://github.com/user-attachments/assets/4d689d0c-3a5e-4089-a9bc-29ab62ad8500)

2.เช็คค่า ``` CC ``` ที่ผู้ใช้เลือกจาก ``` choice ``` และอายุรถที่กรอกค่ามา 

![image](https://github.com/user-attachments/assets/4365f841-cd60-4377-b45f-4f17fb36f45e)

* เช่น หาก ผู้ใช้เลือก ``` choice ที่ 1 ``` ก็จะนำมาคำนวณในเงื่อนไขนี้

![image](https://github.com/user-attachments/assets/d1935a45-9e95-48fa-8634-c801b07fb856)

``` base_tax = 1200 ```

และหากผู้ใช้กรอกอายุรถในช่วง 6-10 ปี ก็จะนำหาค่าลดหย่อนว่า ได้ลดกี่เปอร์เซ็นต์ และ ราคาที่ต้องจ่ายภาษีรถยนต์จริง ๆ กี่บาท

* เช่น ผู้ใช้กรอก``` อายุรถ 6 ปี ```

![image](https://github.com/user-attachments/assets/433351ea-bdb7-4e46-9b58-d91336c1ab85)

จากเงื่อนไขนี้ คือ ``` car_age = 6 ``` ,``` discount_rate = (6 - 5) * 10 = 10 ``` <== หาเปอร์เซ็นต์, ``` tax =  1200 * (100 - 10) / 100 = 1080 ```

* ดังนั้นราคาที่ต้องจ่ายหลังลดหย่อนภาษี คือ 1080 บาท

## FlowChart

Link :[https://miro.com/app/board/uXjVL6MqAIw=/](https://miro.com/welcomeonboard/NDZCSHhXdDhocC9GU3JvM1FsZlp2Tm1hUi9zU3pDWlhLT3BVQXZEZXIzc1lrZWdTYXdIYjBielNScWxpS2dkQU95Z3dBc1B6RkNsRTB4dXN0eUR6MmtLUG5sZXFYY014UmFLUU1nTzBSd2xJa3M4MU8yazZSY2dzT1hEUE44UjIhZQ==?share_link_id=120872289430)

## สมาชิก

    1.นายจิณณวัตร ปัจฉิม  465415241002 

    2.นายวรรธนัย กิ่งไทร   465415241012

    CSS46541N

( [โปรแกรมคำนวณภาษีรถยนต์ 4 ประตู](#โปรแกรมคำนวณภาษีรถยนต์-4-ประตู) ) <== กดเพื่อกลับด้านบน



