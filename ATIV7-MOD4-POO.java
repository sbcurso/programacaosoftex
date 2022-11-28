package br.com.meu pacote

public class Exception {

    public static void main(String [] args) {
        
        try{
            int[] vetor = new int [4];
            
            System.out.println("Antes da exception");
        
            vetor[4] = 1;
        
            System.out.println("Esse texto nao sera impresso"); 
       }  catch(exception.java exception){
           System.out.println("Excecao ao acessar indice do vetor q nao existe ");
       }  
            
        System.out.println("esse texto sera impresso apos a exception");    
    }
       
}       