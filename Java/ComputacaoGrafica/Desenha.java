package TrabalhoCG;
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JPanel;

public class Desenha extends JPanel{
	int pixels[][] ;
	int altura,largura;
	public  Desenha(int altura,int largura) {
		pixels=new int[altura][largura];
		this.altura=altura;
		this.largura=largura;
	}
	public  Desenha() {
		pixels=new int[600][600];
		this.altura=600;
		this.largura=600;
	}
	private Lados lados[];
    private Vx vx[];
    int px1=50, px2=250, px3=210, px4=200,
            py1=50, py2=50, py3=200, py4=200; 
	@Override
	
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
          
        lados = new Lados[4];
        vx = new Vx[312];
        for(int i=0;i<312;i++) vx[i] = new Vx();
        
    }
	 public void limpa(Graphics g) {
		 for(int i=0;i<altura;i++) {
			 for(int j=0;j<largura;j++) {
				 pixels[j][i]=0;
			 }
		 }
	}
	public void limpa() {
		Graphics g = getGraphics();
		 for(int i=0;i<altura;i++) {
			 for(int j=0;j<largura;j++) {
				 //g.setColor(Color.white);
				 //putPixel(g, j, i);
				 pixels[j][i]=0;
			 }
		 }
	}
	public void poligono(Graphics g) {
       algBres(g,150,150,200,150);
       algBres(g,200,150,210,180);
       algBres(g,210,180,175,175);
       algBres(g,175,175,185,210);
       
       algBres(g,185,210,150,200);
       algBres(g,150,200,150,150);
   }
	
	private void criaLados() {
	        
	        lados[0] = new Lados(1,49,50,50,200);
	        lados[1] = new Lados(2,50,200,250,-0.2666);
	        lados[2] = new Lados(3,200,210,210,-1);
	        lados[3] = new Lados(4,49,200,50,0.9375);
	   }
	
    public void algDDA(Graphics g, int xi, int yi, int xf, int yf) {

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
    public void algBres(Graphics g, int xi, int yi, int xf, int yf) {
        
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
    
    public void algBresCir(Graphics g, int raio, int xi, int yi) {
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
    
    
    public void preVarred(Graphics g, int xmin, int ymin, int xmax, int ymax) {
        boolean liga;
        
        for (int y=ymin-1; y<=ymax+1; y++) {
            liga = false;
            for(int x=xmin-1; x<=xmax+1; x++) {
                if (liga) putPixel(g,x,y);
                if((pixels[x+1][y] > 0)&(pixels[x+2][y]<1)) liga = !liga;
                
                
            }
        }
    }
    
    public void preBF(Graphics g, int x, int y) {
    	if((x<altura &&x>=0)&&(y<largura &&y>=0)) {
    		if (pixels[x][y]== 0) {
                putPixel(g,x,y);
                preBF(g,x+1,y);
                preBF(g,x-1,y);
                preBF(g,x,y+1);
                preBF(g,x,y-1);
            }
    	}
        
    }
    
    
    public void preAGeo(Graphics g) {
        
        int x;
        for(int i=0;i<4;i++) {
            for(int yvar=lados[i].ymin; yvar<=lados[i].ymax; yvar++) {
               x = (int) (lados[i].um_s_m * (yvar - lados[i].ymin) + lados[i].xymin);
               if(vx[yvar].x1== -1) vx[yvar].x1 = x;
               else vx[yvar].x2= x;
            }
         }
        ordernaVx();
        imprimeVx(g);
        
    }
    
    private void ordernaVx() {
        for (int y=0; y<312; y++)
        {
            int aux =vx[y].x1;
            if(vx[y].x1 > vx[y].x2) {
                vx[y].x1 =vx[y].x2;
                vx[y].x2 = aux;
            }
        }
        
    }

    private void imprimeVx(Graphics g) {
        for (int y=0; y<312; y++) {
            if(vx[y].x1 != -1) {
                  algBres(g,vx[y].x1,y,vx[y].x2,y);
            }
        }
        
    }
    
    public class Lados {
        
        int lado;
        int ymin;
        int ymax;
        int xymin;
        double um_s_m;

        public Lados() {
            this(0,0,0,0,0.0);
        }

        public Lados(int lado, int ymin, int ymax, int xymin, double um_s_m) {
            this.lado = lado;
            this.ymin = ymin;
            this.ymax = ymax;
            this.xymin = xymin;
            this.um_s_m = um_s_m;
        }
        
        
    }

  public class Vx {
        
        int x1;
        int x2;

        public Vx() {
            this.x1 = -1;
            this.x2 = -1;
        }
    }
  
    public void putPixel(Graphics g, int x, int y) {
    	if((x < largura && y < altura)&&(0 <= x && 0 <= y)) {
    		g.drawLine(x, y, x, y);
            pixels[x][y]=1;
    	}
    }
}
