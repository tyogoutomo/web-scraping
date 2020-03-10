import os, time

from tqdm import tqdm
from google_screenshot import GoogleCrawler
from yahoo_screenshot import YahooCrawler
from bing_screenshot import BingCrawler
# from instagram_screenshot import InstagramCrawler
# from face_cropper_mtcnn import mtcnnCropper

# out_path = '/media/luqmanr/TOSHIBA1TB/Thailand'
out_path = '/media/luqmanr/TOSHIBA1TB/Thailand'

daftar_nama = [
  "ธนา ลิมปยารยะ",
  "ธนา สุทธิกมล",
  "ธนากร โปษยานนท์",
  "ธนากร ศรีบรรจง",
  "ธนิตย์ จิตนุกูล",
  "ธฤษณุ สรนันท์",
  "ธัชพล เสือทองคำ",
  "ธันวา สุริยจักร",
  "ธานินทร์ ทัพมงคล",
  "ธารา ทิพา",
  "ธาวิน เยาวพลกุล",
  "ธิติ มหาโยธารักษ์",
  "ธีธัช จรรยาศิริกุล",
  "ธีธัช รัตนศรีทัย",
  "ธีร์ วณิชนันทธาดา",
  "ธีรดนย์ ศุภพันธุ์ภิญโญ",
  "ธีรเดช เมธาวรายุทธ",
  "ธีรภัทร โลหนันทน์",
  "นพชัย ชัยนาม",
  "นพฤทธิ์ ศรีบุตร",
  "นภัทร อินทร์ใจเอื้อ",
  "นรภัทร วิไลพันธุ์",
  "นรินทร์ ภูวนเจริญ",
  "นันทวัฒน์ อาศิรพจนกุล",
  "นาท ภูวนัย",
  "นิธิ สมุทรโคจร",
  "นิธิดล ป้อมสุวรรณ",
  "นินนาท สินไชย",
  "นิรุตติ์ ศิริจรรยา",
  "บรมวุฒิ หิรัญยัษฐิติ",
  "บริบูรณ์ จันทร์เรือง",
  "บัณฑวิช ตระกูลพานิชย์",
  "บ่าววี",
  "เบน อิศรางกูร ณ อยุธยา",
  "เบนจามิน โจเซฟ วาร์นี",
  "ปฐมพงศ์ เรือนใจดี",
  "ปรมะ อิ่มอโนทัย",
  "ปราชญา เรืองโรจน์",
  "ปราโมทย์ เทียนชัยเกิดศิลป์",
  "ปริยะ วิมลโนช",
  "ปวรพัฒน์ จารุศักดิ์วีรกุล",
  "ปองกูล สืบซึ้ง",
  "ปิติพน พรตรีสัตย์",
  "ปิยะวัฒน์ รัตนหรูวิจิตร",
  "ปีเตอร์ คอร์ป ไดเรนดัล",
  "ปีเตอร์ ธูนสตระ",
  "ปีเตอร์ ไนท์"
]

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for nama in daftar_nama:
    GoogleCrawler(nama, out_path)
    YahooCrawler(nama, out_path)
    BingCrawler(nama, out_path)
    # InstagramCrawler(nama, out_path)

    # print("cropping for", nama)
    # nama_path = os.path.join(out_path,nama)
    # filenames = files(nama_path)
    # for filename in filenames:
    #     mtcnnCropper(nama_path, filename)

    time.sleep(50)
