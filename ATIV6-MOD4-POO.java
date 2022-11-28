import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class Box implements Serializable {

 private int largura;
 private int altura;

 public static void main(String[] args) {
  Box myBox = new Box();
  myBox.setLargura(50);
  myBox.setAltura(20);

   try { 
     FileOutputStream fs = new FileOutputStream("foo.ser");
     ObjectOutputStream os = new ObjectOutputStream(fs);
     os.writeObject(myBox);
     os.close();
   }catch (Exception e) {
     e.printStackTrace();
   }
 }

 public void setLargura(int largura) {
   this.largura = largura;
 }

 public void setAltura(int altura) {
   this.altura = altura;
 }
}