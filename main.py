# var
Water = 1.0  # รับค่าระดับน้ำจาก sensor
notifiact = 'แจ้งเตือนระดับนํ้า : '
T1 = 'สูง, อยู่ในระดับเฝ้าระวัง'
T2 = 'อันตราย, เสี่ยงนํ้าท่วม'
noting = 'ไม่มีอะไร'

# code body
if Water >= 1:
    if 1 <= Water < 2:
        print(f'{notifiact}{T1}\n')
    elif Water >= 2:
        print(f'{notifiact}{T2}\n')
else:
    print(f'{notifiact}{noting}\n')