package helloworld;

public class HelloWorld {
	public static void main(String args[]){
		int tong10SoChanDauTien = 0;
		for(int i = 0;i < 20;i+=2){
			tong10SoChanDauTien += i ;
		}
		System.out.print("Tong 10 so chan dau tien la : " + tong10SoChanDauTien);
		int demChiaHetCho7 = 0;
		for(int i = 1;i< 101;++i){
			if (i%7 == 0){
				demChiaHetCho7 += 1;
			}
		}
		System.out.print("\nDem chia het cho 7 : " + demChiaHetCho7 + "\n");
		Double tong = 0.0;
		if (args.length != 10) System.out.print("Nhap lai 10 so di");
		else{
			for (int i = 0; i < args.length; ++i){
				Double j = Double.parseDouble(args[i]);
				tong += j;
			}
			Double tb = tong/args.length;
			System.out.print("tong la : "+tong+"\ntrung binh la : "+tb+ "\n");
		}
	}
}
