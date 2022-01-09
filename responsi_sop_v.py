#RESPONSI SOP V

def menu():
    print("=================Menu=================")
    print("(1). simulasi manajemen ram")
    print("(2). simulasi manajemen penjadwalan")
    print("(3). exit")
    print("======================================")
    
def manajemen_ram():    
    ram =int(input("Masukkan jumlah kapasitas RAM(GB) : "))
    peta =int(input("Masukkan jumlah petabit(GB): "))
    os =int(input("Masukkan jumlah ram yang di gunakan oleh OS(GB): "))
    kp1  =int(input("Masukkan jumlah kapasitas program 1(GB): "))
    kp2  =int(input("Masukkan jumlah kapasitas program 2(GB): "))
     #rumus sisa ram 
    rt1 =(ram - os ) 
    rt2 =(rt1 - kp1)
    rt3 =(rt2 -kp2 )
     #rumus ram terpakai 
    rtp1 =(os + kp1 )
    rtp2 =(rtp1 + kp2)

     #rumus petabit 
    pb = (ram/peta)
    pba =(pb*1024)#mbps
    pbp =(pba*1024)#kbps

    #rumus blok
    blok1 = ram - rtp2
    blok0 = ram - rt3

    print("====================Ikhwan NA====================")
    print("Total RAM: ",ram, "GB")
    print("jumlah petabit: ",peta,"GB")
    print("jumlah kapasitas per petabit: ",pbp,"kbps")
    print("jumlah RAM terpakai: ",rtp2,"GB")
    print("Sisa RAM: ",rt3,"GB")
    print("Jumlah Blok Bernilai 0: ",blok1)
    print("Jumlah Blok Bernilai 1: ",blok0)
    print("==================================================")
def manajemen_lop():
    if __name__ == '__main__':
        print("Masukan jumlah yang akan di hitung : ")
    total_p_no = int(input())
    total_time = 0 
    total_time_counted = 0
    proc = []
    wait_time = 0
    turnaround_time = 0
    for _ in range(total_p_no):
        
        print("Masukan waktu mulai (spasi) lama proses") 
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]
        
        proc.append([arrival, burst, remaining_time, 0])
        
        total_time += burst
    print("Masukan jumlah quantum time")
    time_quantum = int(input())
    
    while total_time != 0:
        
        for i in range(len(proc)):
            
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                
                proc[i][2] = 0 
            elif proc[i][2] > 0:
                
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                turnaround_time += total_time_counted - proc[i][0]
                
                proc[i][3] = 1 
    print("\nRata - rata waktu tunggu : ", (wait_time * 1) / total_p_no)
    print("Rata Rata perputaran waktu : ", (turnaround_time * 1) / total_p_no)

menu()   
pilihan =int(input("Masukkan nomor pilihan: "))

if pilihan == 1:
    manajemen_ram()
elif pilihan == 2:
    manajemen_lop()
elif pilihan == 3:
    print("anda telah keluar")
    exit()
else :
    print("Pilihan anda tidak ada")
    print("Silahkan coba lagi")

    

