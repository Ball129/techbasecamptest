## Answer of TechBaseCamp Test

Language: Python

### 1. ให้ตั้งตัวแปรขึ้นมาแค่ 2 ตัว และให้สลับค่ากัน โดยห้ามใช้ function ให้แค่ operater พื้นฐานเท่านั้น

#### <u>Solution:</u> [basic_swap.py](./basic_swap.py)

ใช้วิธีการ สลับค่า 3 วิธี
* ใช้ temporary variable (ใช้ได้กับทุก datatype)
* ใช้ สมบัติการบวก / ลบ (ใช้ได้กับ number เท่านั้น)
* ใช้ syntax ของ python (ใช้ได้กับทุก datatype)

#### <u>Result:</u> 

```shell script
Initial a=1, b=2
Now a=2, b=1
Now a=1, b=2
Now a=2, b=1
```

### 2.ให้มีตัวเลข 1-100,000 แบบเรียงสลับกัน จากนั้นให้เขียนโปรแกรมหรืออธิบายหลักการที่จะทำให้เลขเรียงกันให้ถูกต้องเช่น  1,3,5,2,4 —> 1,2,3,4,5

#### <u>Solution:</u> [quick_sort_pivot_center.py](./quick_sort_pivot_center.py)

ใช้ algorithm quicksort โดยใช้ค่า pivot จาก median of three (ค่าซ้ายสุด, กลาง, ขวาสุด) 
เพื่อให้ได้ performance ที่ใกล้เคียงค่าสูงสุด O(n log n) มากที่สุด โดยสังเกตจากจำนวนครั้งที่ทำการสลับค่า (swap)

โดยจุุดเด่นของ quicksort คือ 
* เข้าใจง่าย ไม่ซับซ้อน 
* มี performance ในระดับกลาง เมื่อเทียบกับ algorithm แบบอื่นๆ (Best-Average: O(n log n), Worst: O(n^2))
* สามารถสลับค่าในตัว array ได้เลย โดยไม่ต้องการเนื้อที่ในการเก็บ array เพิ่ม

ข้อควรระวัง
* Performance ขึ้นอยู่กับการเลือก pivot เป็นส่วนใหญ่ โดยควรให้ใกล้เคียงค่า median ที่สุด

#### <u>Result:</u> 

```shell script
Start test performance 50 times.
Sorting 100000 numbers (1 - 100000)
Loop 0:> Total time: 0.42 s (422.24 times of builtin sorted)
Loop 0:> Max recursive depth 40
Loop 0:> Total swap 466076

Sorting 100000 numbers (1 - 100000)
Loop 10:> Total time: 0.41 s (251.46 times of builtin sorted)
Loop 10:> Max recursive depth 41
Loop 10:> Total swap 465111

Sorting 100000 numbers (1 - 100000)
Loop 20:> Total time: 0.42 s (265.37 times of builtin sorted)
Loop 20:> Max recursive depth 39
Loop 20:> Total swap 464169

Sorting 100000 numbers (1 - 100000)
Loop 30:> Total time: 0.41 s (262.59 times of builtin sorted)
Loop 30:> Max recursive depth 39
Loop 30:> Total swap 460759

Sorting 100000 numbers (1 - 100000)
Loop 40:> Total time: 0.41 s (269.24 times of builtin sorted)
Loop 40:> Max recursive depth 39
Loop 40:> Total swap 458991

Average time: 0.43 s (246.28 times of builtin sorted)
Average recursive depth 39.97
Average swap 464788.66
```

อ้างอิง: https://en.wikipedia.org/wiki/Quicksort , https://www.geeksforgeeks.org/quick-sort/

