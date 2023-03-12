
CarlosHenrique05
/
CaomputacaoGrafica
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
CaomputacaoGrafica/Janela.java
@CarlosHenrique05
CarlosHenrique05 Create Janela.java
 1 contributor
180 lines (147 sloc)  5.18 KB
package com.mycompany.trabalhocg;

import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Janela extends JFrame {
    public int pixels[][] = new int[600][600];
    
    public Janela() {
        this.setTitle("Titulo");
        this.setLocationRelativeTo(null);
        this.setVisible(true);
        this.setSize(600, 600);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        JPanel painel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                int v=150;    
                
                g.setColor(Color.RED);
                algAnalitico(g,50,50,150,150); //45º
                algAnalitico(g,50,50,150,50); // 0º
                algAnalitico(g,50,50,50,150); //90º
                algAnalitico(g,50,50,150,100); //67,5º
                algAnalitico(g,50,50,100,150); //112,5º
              
                
                g.setColor(Color.GREEN);       
                algDDA(g,50+v,50,150+v,150);
                algDDA(g,50+v,50,150+v,150); //45º
                algDDA(g,50+v,50,150+v,50); // 0º
                algDDA(g,50+v,50,50+v,150); //90º
                algDDA(g,50+v,50,150+v,100); //67,5º
                algDDA(g,50+v,50,100+v,150); //112,5º
                
                g.setColor(Color.BLUE);
                algBres(g,50+2*v,50,150+2*v,150); //45º
                algBres(g,50+2*v,50,150+2*v,50); // 0º
                algBres(g,50+2*v,50,50+2*v,150); //90º
                algBres(g,50+2*v,50,150+2*v,100); //67,5º
                algBres(g,50+2*v,50,100+2*v,150); //112,5º
                
                g.setColor(Color.RED);
                algParam(g, 50,50,200);
                
                g.setColor(Color.GREEN);
                algIncSem(g, 50,151,200);
                
                g.setColor(Color.BLUE);
                algBres(g, 50,252,200);
            }
        };

        this.add(painel);
    }

    private void algDDA(Graphics g, int xi, int yi, int xf, int yf) {

        int steps;
        float x = xi, y = yi, incX, incY;

        int dx = xf - xi;
        int dy = yf - yi;

        if (Math.abs(dx) > Math.abs(dy)) {
            steps = Math.abs(dx);
            incX = 1;
            incY = (float) dy / dx;
        } else {
            steps = Math.abs(dy);
            incY = 1;
            incX = (float) dx / dy;
        }

        for (int i = 0; i < steps; i++) {
            x = x + incX;
            y = y + incY;
            putPixel(g, Math.round(x), Math.round(y));
        }

    }

    public void algAnalitico(Graphics g, int xi, int yi, int xf, int yf) {
        float m, b, dy, dx;
        dy = yf - yi;
        dx = xf - xi;
        
        m = (float) dy/dx;
        
        b = (float) (yi - m * xi);
        
        for(int x = xi; x<=xf; x++) {
            int y = (int) (m * x + b);
            putPixel(g,x,y);
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
    
    public void algParam(Graphics g, int raio,int xi,int yi) {
        int x, y;
        for (int ang=0; ang<360; ang++) {
            System.out.println("Loops: "+ang);
            x = (int) (raio * Math.cos(Math.PI*ang/180));
            y = (int) (raio * Math.sin(Math.PI*ang/180));
            putPixel(g,x+xi,y+yi);
        }
    }
    
    public void algIncSem(Graphics g, int raio,int xi,int yi) {
        int x=0, y=0;
        double ang=0.0;

        while(ang<=2*Math.PI) {
            x = (int) (raio * Math.cos(ang))+xi;
            y = (int) (raio * Math.sin(ang))+yi;
            putPixel(g,x,y);
            ang = ang + (double) 1/raio; 
        }
    }
    
    public void algBres(Graphics g, int raio, int xi, int yi) {
        int x = 0, y = raio, u = 1, v = 2 * raio - 1, e = 0;

        while (x <= y) {            
            putPixel(g, x + xi, y + yi);
            putPixel(g, y + xi, x + yi);
            putPixel(g, -x + xi, y + yi);
            putPixel(g, -y + xi, x + yi);
            putPixel(g, -x + xi, -y + yi);
            putPixel(g, -y + xi, -x + yi);
            putPixel(g, x + xi, -y + yi);
            putPixel(g, y + xi, -x + yi);

            x++;
            e = e + u;
            u = u + 2;
            if (v < (2 * e)) {
                y--;
                e = e - v;
                v = v - 2;
            }
        } 
    }

    public void putPixel(Graphics g, int x, int y) {
        g.drawLine(x, y, x, y);
        pixels[x][y]=1;
    }
}
