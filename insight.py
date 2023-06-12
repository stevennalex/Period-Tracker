#INSIGHT
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk


#OLAHRAGA

def link_olahraga():
    youtube_link = "https://www.youtube.com/watch?v=kB96HXtDkrs"
    webbrowser.open(youtube_link)

def olahraga():
    window = tk.Toplevel()
    window.resizable(False,False)
    window.configure(bg='lightpink')
    window.geometry('600x600')

    image = Image.open("bg4.jpg")
    image = image.resize((600, 900)) 
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    text = tk.Label(window, text='''    Seperti yang kita ketahui, nyeri pada saat haid memang menyebalkan. Namun, hal tersebut dapat kita atasi dengan berolahraga karena saat berolahraga tubuh akan melepaskan hormon endorfin sebagai pereda nyeri alami. Berikut merupakan contoh olahraganya:\n           
    1. Jalan santai
        Olahraga ringan seperti jalan santai terbukti dapat meringankan keluhan yang muncul saat menstruasi, misalnya kram perut, sakit kepala, perut kembung, dan nyeri payudara. Untuk mendapatkan manfaat tersebut, luangkanlah waktu setidaknya 30 menit setiap hari untuk melakukan jalan santai.\n
    2. Berenang
        Berenang merupakan salah satu jenis olahraga yang dapat mengurangi kram dan kelelahan selama haid. Durasi renang yang dianjurkan adalah sekitar 10–30 menit sebanyak 2–5 kali seminggu.\n
    3. Bersepeda
        Bersepeda termasuk olahraga aerobik ringan yang baik untuk mengurangi nyeri haid. Jika rutin dilakukan, bersepeda akan membuat aliran darah lebih lancar dan membuat lebih rileks sehingga nyeri saat haid pun akan berkurang.\n
    4. Yoga
        Yoga merupakan jenis olahraga ringan yang dapat membuat tubuh lebih rileks, menenangkan pikiran, serta mengurangi keluhan nyeri haid. Olahraga yang praktis dan bisa dilakukan di rumah ini terbukti efektif untuk mengurangi gejala nyeri dan stres pada wanita saat haid.\n
    5. Pilates
        Gerakan dalam pilates baik untuk melancarkan aliran darah, meregangkan otot, dan meningkatkan hormon endorfin yang dapat mengurangi nyeri saat haid. Tak hanya itu, olahraga ini pun baik untuk memperkuat otot dan sendi serta meringankan nyeri punggung.\n       
        Klik tombol dibawah untuk menampilkan video referensi dalam berolahraga pada saat nyeri haid:'''
                    ,justify="center", wraplength=390)
    text.pack()
    
    button = tk.Button(window, text="Rekomendasi Olahraga", command=link_olahraga)
    button.pack()

    window.mainloop()

# MAKANAN

def link_makanan():
    youtube_link = "https://youtu.be/V42iKfIMSD8"
    webbrowser.open(youtube_link)

def makanan():
    window = tk.Toplevel()
    window.resizable(False,False)
    window.configure(bg='lightpink')
    window.geometry('600x600')

    image = Image.open("bg5.jpg")
    image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
    image = image.resize((600, 900))  

    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    
    text = tk.Label(window, text='''    Saat mengalami gejala menstruasi yang terbilang ringan, dapat diatasi dengan memakan makanan yang mampu meredakan nyeri haid. Berikut merupakan makanan yang dapat meredakan nyeri haid:
    1.  Brokoli
        Sayuran dengan warna hijau ini mengandung beberapa nutrisi yang terbukti membantu dalam melawan kram menstruasi, seperti vitamin A, C, B6, E, kalsium, kalium, dan magnesium.
    2.  Yoghurt rendah lemak
        Yoghurt rendah lemak merupakan makanan yang kaya akan kalsium dan dianjurkan saat wanita sedang menstruasi. Pada secangkir yoghurt mengandung sumber kalsium yang mampu memenuhi 25 persen dari kebutuhan harian wanita.
    3.  Salmon
        Makanan untuk nyeri haid yang bermanfaat untuk tubuh adalah salmon. Salmon sendiri mengandung vitamin D yang dapat memenuhi kebutuhan harian tubuh, yaitu sebanyak 100 IU. Selain itu, salmon mengandung vitamin B6 yang dapat membantu mengurangi iritabilitas dan nyeri pada payudara.
    4.  Telur
        Telur adalah pendukung nutrisi yang paling baik. Kandungan vitamin D, B6, dan E dalam telur bisa membantu melawan reaksi PMS yang membuat tidak nyaman. Ketiganya mampu mengendalikan senyawa kimia pada otak yang memicu terjadinya PMS.
    5.  Pisang
        Pada saat haid, sering kali kita merasakan kembung pada perut. Hal tersebut dapat diatasi oleh pisang karena pisang yang kaya akan vitamin B6 dan kalium yang meringankan rasa kembung pada perut.
    6.  Teh Chamomile
        Teh chamomile direkomendasikan untuk nyeri haid karena membantu meredakan kejang otot dan mengurangi rasa kram saat menstruasi. Secangkir teh chamomile bebas kafein yang alami membuat PMS tidak terlalu buruk, mengurangi rasa gelisah, sekaligus sifat mudah tersinggung yang disebabkan oleh berubahnya hormon ketika haid datang. 
    7.  Kacang-kacangan
        Kacang-kacangan dapat membantu meredakan gejala nyeri haid, hal ini disebabkan oleh kacang-kacangan yang memiliki kandungan vitamin B6 dan magnesium yang dapat membantu meredakan gejala nyeri haid. Jadi, jangan ragu untuk mengonsumsi kacang maupun selai kacang saat mengalami menstruasi.
        Klik tombol dibawah untuk menampilkan video rekomendasi olahan makanan yang dapat kamu coba saat merasakan nyeri haid:'''
                    ,justify="center", wraplength=450)
    text.pack()

    button = tk.Button(window, text="Rekomendasi makanan", command=link_makanan)
    button.pack()

    window.mainloop()

#TIDUR
def link_tidur():
    youtube_link = "https://youtu.be/YedavoJ7zhc"
    webbrowser.open(youtube_link)

def tidur():
    window = tk.Toplevel()
    window.resizable(False,False)
    window.configure(bg='lightpink')
    window.geometry('600x600')

    image = Image.open("bg6.jpg")
    image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
    image = image.resize((600, 900))  

    photo = ImageTk.PhotoImage(image)

    background_label = tk.Label(window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    text = tk.Label(window, text='''    Posisi tidur dapat mengurangi rasa nyeri yang dirasakan saat menstruasi. Posisi tidur yang nyaman berfungsi untuk mengurangi rasa kram atau nyeri haid. Namun, posisi tidur yang berbeda memiliki manfaat yang berbeda pula. Berikut adalah posisi tidur yang dapat anda coba untuk membantu mengurangi atau meredakan nyeri haid:

    1. Posisi fetal
        Posisi fetal atau janin mempunyai banyak manfaat untuk tubuh. Caranya adalah dengan meringkuk. Posisikan tubuh secara menyamping, kemudian tekuk kaki lalu pastikan lutut sejajar dengan dada. Ini merupakan posisi yang bagus untuk punggung bagian bawah yang terasa nyeri akibat menstruasi sehingga dapat mengurangi tekanan pada tulang belakang. Selain itu, posisi tidur fetal mampu melemaskan otot-otot sekitar perut dan bokong serta mengurangi ketegangan dan nyeri sehingga dapat membantu untuk tidur.

    2. Telentang dengan bantal di bawah lutut
        Posisi tidur telentang juga dapat membantu untuk mengurangi nyeri haid. Posisi tidur ini dapat melindungi tulang belakang sekaligus meredakan nyeri pinggang atau punggung. Apalagi, posisi tidur telentang menggunakan gravitasi untuk menjaga tubuh tetap sejajar di atas tulang belakang.

    3. Posisi menyamping dengan bantal di paha
        Seperti posisi fetal, tidur menyamping dapat mengurangi nyeri atau kram punggung yang sering terjadi saat periode haid. Dikarenakan posisi ini dapat mengurangi tekanan pada tulang belakang. Agar terasa lebih nyaman, bisa juga menaruh bantal di antara kedua paha Anda.

    4. Child’s pose
        Child’s pose juga bisa diterapkan sebagai posisi tidur nyaman saat periode menstruasi datang. Child’s pose digambarkan sebagai tidur dengan posisi seperti sujud, tetapi dengan posisi dada hingga menyentuh paha. Bayi sering mempraktikkan posisi ini saat ia tertidur. Child’s pose diyakini dapat merilekskan punggung yang kerap terasa nyeri dan meredakan sakit kepala yang sering muncul saat haid. Posisi ini juga diyakini dapat menenangkan pikiran.
        
        Klik tombol dibawah untuk menampilkan video referensi dari posisi tidur yang membuat terasa lebih nyaman saat haid:
    '''
                    ,justify="center", wraplength=450)
    text.pack()

    button = tk.Button(window, text="Rekomendasi posisi tidur", command=link_tidur)
    button.pack()

    window.mainloop()
