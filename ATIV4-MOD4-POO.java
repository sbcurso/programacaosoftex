package MeuPacote;

public class MinhaClasse {
    public void meuMetodo(){
        System.out.println("Esse e o meu pacote!");
    }  
}
public class NovaClasse {
    public String novoMetodo(){
      String name = "So para exemplo";
      return name;
    }
}

import MeuPacote.MinhaClasse;
import MeuPacote.NovaClasse;

public class MeuPrograma {
  public static void main(String[] args) {
   MinhaClasse obj = new MinhaClasse();
   NovaClasse obj2 = new NovaClasse();
   obj.meuMetodo();
   System.out.println(obj2.novoMetodo());
  }
}
import MeuPacote.*;

public class MeuPrograma {
  public static void main(String[] args) {
   MinhaClasse obj = new MinhaClasse();
   NovaClasse obj2 = new NovaClasse();
   obj.meuMetodo();
   System.out.println(obj2.novoMetodo());
  }
}