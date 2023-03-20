package javaapplication16;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Janela extends JFrame{
    int pixels[][] = new int[600][600];
    int coordenadas[][] =new int[180][2];
    int xma,xmi,yma,ymi;
    public Janela() {
	this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	this.setBounds(0, 0, 600, 600);
	this.setResizable(false);
        this.setVisible(true);
        
        JPanel painel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                g.setColor(Color.RED);
                algParam(g, 180,200,200);
            }
        };

        this.add(painel);
    }
      
    protected void paintComponent(Graphics g) {
        
        
    }
    
    public void algParam(Graphics g, int raio,int xi,int yi) {
        int x, y;
        int temp=0;
        for (int ang=0; ang<360; ang+=2) {
            coordenadas[temp][0]=(int) (raio * Math.cos(Math.PI*ang/180))+xi;
            coordenadas[temp][1]=(int) (raio * Math.sin(Math.PI*ang/180))+yi;  
            System.out.println((int) (180 * Math.sin(Math.PI*358/180))+yi);
            System.out.println((int) (180 * Math.cos(Math.PI*358/180))+xi);
            putPixel(g,coordenadas[temp][0],coordenadas[temp][1]);
            if(temp>0){
                algBres(g, coordenadas[temp][0],coordenadas[temp][1],coordenadas[temp-1][0],coordenadas[temp-1][1]);
                if(coordenadas[temp][0] > xma){
                    xma=coordenadas[temp][0];
                }else{
                    if(coordenadas[temp][0]<xmi){
                        xmi=coordenadas[temp][0];
                    }
                }
                if(coordenadas[temp][1] > yma){
                    yma=coordenadas[temp][1];
                }else{
                    if(coordenadas[temp][1]<ymi){
                        ymi=coordenadas[temp][1];
                    }
                }
            }else{
                coordenadas[179][0]=(int) (raio * Math.cos(Math.PI*358/180))+xi;
                coordenadas[179][1]=(int) (raio * Math.sin(Math.PI*358/180))+yi;  
                algBres(g, coordenadas[temp][0],coordenadas[temp][1],coordenadas[179][0],coordenadas[179][1]);
                xma=coordenadas[0][0];
                xmi=coordenadas[0][0];
                yma=coordenadas[0][1];
                ymi=coordenadas[0][1];
            }
            temp+=1;     
        }
        preVarred(g,xmi,ymi,xma,yma);  
       
    }
    
    public void preVarred(Graphics g, int xmin, int ymin, int xmax, int ymax) {
        boolean liga;
        
        for (int y=ymin-1; y<=ymax+1; y++) {
            liga = false;
            for(int x=xmin-1; x<=xmax+1; x++) {
                if (liga) putPixel(g,x,y);
                if(x+2<600){if((pixels[x+1][y] > 0)&(pixels[x+2][y]<1)) liga = !liga;}
                
                
                
            }
        }
    }
     
    private void algBres(Graphics g, int xi, int yi, int xf, int yf) {
        
       int x = xi, y = yi, d=0, dx = xf-xi, dy = yf-yi, c, m, incX=1, incY=1;
       
       if(dx < 0) {incX = -1; dx = -dx;}
       if(dy < 0) {incY = -1; dy = -dy;}
       
       if(dy <= dx) {
           c = 2 * dx; m = 2 * dy;        
           for(;;) {
               putPixel(g,x,y);
               if (x == xf) break;
               x += incX;
               d += m;
               if(d >= dx) {y += incY; d -= c;}
           }
       }else{
           c = 2 * dy; m = 2 * dx;
           for(;;) {
               putPixel(g,x,y);
               if (y == yf) break;
               y += incY;
               d += m;
               if(d >= dy) {x += incX; d -= c;}
            }       
        }
    }
    
 
    public void putPixel(Graphics g, int x, int y) {
    	if((x < 600 && y < 600)&&(0 <= x && 0 <= y)) {
            g.drawLine(x, y, x, y);
            pixels[x][y]=1;
    	}
    }
}
