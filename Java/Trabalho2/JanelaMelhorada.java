package TrabalhoCG;

import javax.swing.JButton;
import javax.swing.JMenu;
import java.awt.event.KeyAdapter;
import java.util.Vector;
import javax.swing.JDesktopPane;
import javax.swing.JComboBox;
import javax.swing.JMenuBar;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.Graphics;
import java.awt.Canvas;
import java.awt.event.MouseEvent;
import javax.swing.JMenuItem;
import java.awt.Dimension;
import static javax.swing.WindowConstants.EXIT_ON_CLOSE;
import javax.swing.JFrame;
import javax.swing.JComponent;
import javax.swing.JToolBar;
import javax.swing.JPanel;
import java.awt.Cursor;
import java.awt.Color;
import java.awt.Component;
import java.awt.Polygon;
import java.awt.event.KeyEvent;


public class Janela extends JFrame {
	int opcoes[]= new int[2];

	Recorte desenho = new Recorte();

    
   
    public void MudarPanel(int i, int j,int cursor) {
    	opcoes[0]=i;
      opcoes[1]=j;
      mudar_cursor(cursor); 
      repaint();
    }
    public void MudarPanel(int i, int j) {
    	opcoes[0]=i;
      opcoes[1]=j;
      mudar_cursor(2); 
      repaint();
    }
    
	public Janela(int altura,int largura) {

        this.add(desenho);
        MudarPanel(0,0);
        //configurando a janela
        this.setTitle("Algoritmo de Recorte de Retas de Cohen-Sutherland");
        this.setSize(altura,largura);
        this.setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
	    this.setLocationRelativeTo(null);
	    this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	    this.setVisible(true);
        this.setResizable(false);
        setTitle("Trabalho CG");
        

	
	    JPanel panel = new JPanel();

		
	    panel.setBounds(0, 0, altura, largura);
		getContentPane().add(panel);
		panel.setLayout(null);
		

		
        //Menu de barra
        JMenuBar menuBar = new JMenuBar();
        setJMenuBar(menuBar);
				
		
        //Recortes
        JMenu recortes = new JMenu("Rercortes");
        menuBar.add(recortes);
        
        
        //linhas	
        JMenu r1 = new JMenu("Linhas Retas");
        JMenu r2 = new JMenu("Poligonos");

        recortes.add(r1);
        recortes.add(r2);

            r1.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {

                    MudarPanel(0, 0, 1);

                }
            });	
            r2.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    MudarPanel(0, 1, 1);

                }
            });


        //Curvas
        JMenu curvas = new JMenu("Curvas");
        menuBar.add(curvas);


        JMenu c1 = new JMenu("Bézier");
        JMenu c2 = new JMenu("B-Spilner");

        curvas.add(c1);
        curvas.add(c2);

            c1.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    MudarPanel(1, 0, 0);
                }
            });	
            c2.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    MudarPanel(1, 1, 0);
                }
            });
				
					
        //Transformações
        JMenu transformacoes = new JMenu("Transformações");
        menuBar.add(transformacoes);

        JMenu t1 = new JMenu("Translação");
        JMenu t2 = new JMenu("Escala");
        JMenu t3 = new JMenu("Rotação");

        transformacoes.add(t1);
        transformacoes.add(t2);
        transformacoes.add(t3);

            t1.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    MudarPanel(2, 0, 0);
                }
            });	
            t2.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    MudarPanel(2, 1, 0);
                }
            });
            t3.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    MudarPanel(2, 2, 0);
                }
        });
		
        JMenu limpar = new JMenu("Limpar");
        menuBar.add(limpar);

            limpar.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    System.out.println("Teste");
                }
            });
    }
	getContentPane().setLayout(null);
    this.setVisible(true);
    
    void mudar_cursor(int i) {
      if(i == 1) {
        this.setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
      }else {
        setCursor(Cursor.getDefaultCursor());

      }

    }
    class Recorte extends JComponent {
      Vector<Ponto2D> pts2 = new Vector<Ponto2D>();
          int np2 = 0;
          Polygon poly2 = new Polygon();
          double tx=1, ty=1, ang=0.1;
          double mi[][] =  new double[3][2];;
          double mt[][] = new double[2][2];
          double mr[][] = new double[3][2];

          boolean pronto2 = false;

      Poly poly = null;
        int x0, y0; 
        boolean pronto1 = true;
        Ponto2D[] pts = new Ponto2D[4];
        int np1=0;

          float xmin, xmax, ymin, ymax, rWidth = 10.0F, rHeight = 7.5F, pixelSize;
          int maxX, maxY, centerX, centerY, np=0;

          public void pushMatrix() {
              for(int i=0; i<3; i++)
                  for(int j=0; j<2; j++)
                      mi[i][j] = mr[i][j];
          }


          public float fx(int x) {
            return (x - centerX) * pixelSize; 
          }

          public float fy(int y) {
             return (centerY - y) * pixelSize;
          }

          int iX(float x) {
              return Math.round(centerX + x / pixelSize);
          }
          int iY(float y) {        	
            return Math.round(centerY - y / pixelSize);            
          }



          public Recorte() {
            iniciaMatrizes();
              addMouseListener(new MouseAdapter() {
              public void mousePressed(MouseEvent evt) {
                if(opcoes[0]==0) {
                  if(opcoes[1]==0) {
                    float x = fx((evt.getX())), y = fy(evt.getY());
                        if (np == 2) np = 0;
                        if (np == 0) {xmin = x; ymin = y;}
                        else {
                            xmax = x; ymax = y;
                            if (xmax < xmin) {
                                float t = xmax;
                                xmax = xmin;
                                xmin = t;
                            }
                            if (ymax < ymin) {
                                float t = ymax;
                                ymax = ymin;
                                ymin = t;
                            }
                        }
                        np++;
                  }else {
                    int x = evt.getX(), y = evt.getY();
                          if (pronto1) {
                              poly = new Poly();
                              x0 = x; y0 = y;
                              pronto1 = false;
                          }
                          if (poly.size() > 0 && Math.abs(x - x0) < 3 && Math.abs(y - y0) < 3) 
                                  pronto1 = true;
                          else
                              poly.addVertex(new Ponto2D(fx(x), fy(y)));
                  }

                  }else {
                  if(opcoes[0]==1) {
                      if(opcoes[1]==0) {
                        float x = fx(evt.getX()), y = fy(evt.getY());
                              if (np1 == 4) np1 = 0;
                              pts[np1++] = new Ponto2D(x,y);
                      }else {
                        float x= fx(evt.getX()), y = fy(evt.getY());
                              if(pronto2) {
                                  pts2.removeAllElements();
                                  np2 = 0;
                                  pronto2 = false;
                              }
                              pts2.addElement(new Ponto2D(x,y));
                              np2++;
                      }
                  }else {
                    if(opcoes[1]==0) {
                      transformaTranslada(); tx=tx+1; ty=ty+1;
                    }else {
                    if(opcoes[1]==1) {

                      transformaEscala();
                    }else {

                      transformaRotacao(); ang=ang+0.1;
                    }
                    }

                  }

                  }
                repaint();
              }
          });
           addKeyListener(new KeyAdapter() {
                  public void keyTyped(KeyEvent evt) {
                     evt.getKeyChar();
                     if (np2 >= 4) pronto2 = true;
                     repaint();
                  }
            });
          }
          public void transformaEscala() {

              mt[0][0] = (double) 1.5; mt[0][1] = (double) 0;
              mt[1][0] = (double) 0; mt[1][1] = (double) 1.5;



              mr[0][0] =(mi[0][0] * mt[0][0]) + (mi[0][1] * mt[0][1]);
              mr[0][1] =(mi[0][0] * mt[0][1]) + (mi[0][1] * mt[1][1]);

              mr[1][0] =(mi[1][0] * mt[0][0]) + (mi[1][1] * mt[0][1]);
              mr[1][1] =(mi[1][0] * mt[0][1]) + (mi[1][1] * mt[1][1]);

              mr[2][0] =(mi[2][0] * mt[0][0]) + (mi[2][1] * mt[0][1]);
              mr[2][1] =(mi[2][0] * mt[0][1]) + (mi[2][1] * mt[1][1]);

            pushMatrix();

          }
          public void transformaRotacao() {

              double cos = Math.cos(ang);
              double sen = Math.sin(ang);

              mr[0][0] =(mi[0][0] * cos) - (mi[0][1] * sen);
              mr[0][1] =(mi[0][0] * sen) + (mi[0][1] * cos);

              mr[1][0] =(mi[1][0] * cos) - (mi[1][1] * sen);
              mr[1][1] =(mi[1][0] * sen) + (mi[1][1] * cos);

              mr[2][0] =(mi[2][0] * cos) - (mi[2][1] * sen);
              mr[2][1] =(mi[2][0] * sen) + (mi[2][1] * cos);

             pushMatrix();

          }
          public void transformaTranslada() {

              mr[0][0] =(mi[0][0] + tx);
              mr[0][1] =(mi[0][1] + ty);

              mr[1][0] =(mi[1][0] + tx);
              mr[1][1] =(mi[1][1] + ty);

              mr[2][0] =(mi[2][0] + tx);
              mr[2][1] =(mi[2][1] + ty);

              pushMatrix();

          }

          private void iniciaMatrizes() {
              poly2 = new Polygon();

              mi[0][0] = 150; mi[0][1] = 100;
              mi[1][0] = 20; mi[1][1] = 200;
              mi[2][0] = 120; mi[2][1] = 200;



          }
          int clipCode(float x, float y) {
           return (x < xmin ? 8 : 0) | (x > xmax ? 4 : 0) | (y < ymin ? 2 : 0) | (y > ymax ? 1 : 0);    
          }

          void clipLine(Graphics g, float xi, float yi, float xf, float yf, float xmin, float ymin, float xmax, float ymax) {
              int cP = clipCode(xi, yi), cQ = clipCode(xf, yf);
              float dx, dy;
              while((cP | cQ) != 0) {
                  if ((cP & cQ) != 0) return;
                  dx = xf - xi; dy = yf - yi;
                  if (cP != 0) {
                      if ((cP & 8) == 8) {
                       yi = yi + (xmin - xi) * dy / dx;
                       xi = xmin;
                  } else if ((cP & 4) == 4) {
                       yi = yi + (xmax - xi) * dy / dx;
                       xi = xmax;
                  } else if ((cP & 2) == 2) {
                       xi = xi + (ymin - yi) * dx / dy;
                       yi = ymin;
                  } else if ((cP & 1) == 1) {
                       xi = xi + (ymax - yi) * dx / dy;
                       yi = ymax;
                  }

                      cP = clipCode(xi,yi);
                  } else if (cQ != 0) {
                     if ((cQ & 8) == 8) {
                       yf = yf + (xmin - xf) * dy / dx;
                       xf = xmin;
                  } else if ((cQ & 4) == 4) {
                       yf = yf + (xmax - xf) * dy / dx;
                       xf = xmax;
                  } else if ((cQ & 2) == 2) {
                       xf = xf + (ymin - yf) * dx / dy;
                       yf = ymin;
                  } else if ((cQ & 1) == 1) {
                       xf = xf + (ymax - yf) * dx / dy;
                       yf = ymax;
                  }
                     cQ = clipCode(xf,yf);
                  }
              }
              drawLine(g,xi,yi,xf,yf);
          }



          @Override
          public void paint (Graphics g) {

            if(opcoes[0]==0) {
              if(opcoes[1]==0) {
                initValues();
                    if ((np ==0)||(np==1)) drawLine(g,-4,3,4,-3);
                    clipLine(g,-4,3,4,-3,xmin,ymin,xmax,ymax);
                    if (np == 1) {
                        drawLine(g,fx(0),ymin,fx(maxX),ymin);
                        drawLine(g,xmin,fy(0),xmin,fy(maxY));
                    } else if (np == 2) {
                        drawLine(g,xmin, ymin, xmax, ymin);
                        drawLine(g,xmax, ymin, xmax, ymax);
                        drawLine(g,xmax, ymax, xmin, ymax);
                        drawLine(g,xmin, ymax, xmin, ymin);

                    }
              }else {
                initValues();
                    float xmin = -rWidth / 3, xmax = rWidth / 3,
                            ymin = -rHeight /3, ymax = rHeight / 3;

                    g.setColor(Color.blue);
                    drawLine(g,xmin, ymin, xmax, ymin);
                    drawLine(g,xmax, ymin, xmax, ymax);
                    drawLine(g,xmax, ymax, xmin, ymax);
                    drawLine(g,xmin,ymax, xmin, ymin);
                    g.setColor(Color.red);
                    if (poly == null) return;
                    int n = poly.size();
                    if (n == 0) return;
                    Ponto2D pi = poly.vertexAt(0);
                    if (!pronto1) {
                        g.drawRect(iX(pi.x) -2, iY(pi.y) -2, 4, 4);
                        for (int i = 1; i< n; i++) {
                            Ponto2D pp = poly.vertexAt(i);

                            g.drawLine(iX(pi.x), iY(pi.y), iX(pp.x), iY(pp.y));
                            pi = pp;
                        }
                    }
                    else {
                        poly.clipPoli(xmin,ymin, xmax, ymax);
                        drawPoly(g, poly);
                    }
              }

            }else {
            if(opcoes[0]==1) {
                if(opcoes[1]==0) {
                  initValues();
                      int left = iX(-rWidth / 2), right = iX(rWidth / 2), 
                              bottom = iY(-rHeight / 2), top = iY(rHeight / 2);
                      g.drawRect(left, top, right - left, bottom - top);
                      for (int i=0; i < np1; i++) {
                          g.drawRect(iX(pts[i].x)-2, iY(pts[i].y)-2, 4, 4);
                          if (i > 0) g.drawLine(iX(pts[i-1].x), iY(pts[i-1].y), iX(pts[i].x), iY(pts[i].y));
                      }
                      if (np1 == 4) geraCurva(g,pts[0], pts[1], pts[2], pts[3]);	
                }else {
                  initValues();
                      g.setColor(Color.blue);
                      int left = iX(-rWidth / 2), right = iX(rWidth /2), 
                           bottom = iY(-rHeight / 2 ), top = iY(rHeight / 2);
                      g.drawRect(left, top, right - left, bottom - top);
                      Ponto2D[] p = new Ponto2D[np2];
                      pts2.copyInto(p);
                      if(!pronto2) {
                          for (int i=0; i < np2; i++) {
                              g.setColor(Color.black);
                              //g.drawRect(iX(p[i].x) -2, iY(p[i].y) - 2, 4, 4);
                              if (i > 0) {
                                //g.drawLine(iX(p[i-1].x), iY(p[i-1].y), iX(p[i].x), iY(p[i].y));

                              }
                        }
                      }
                      if (np2 >= 4) { g.setColor(Color.red);geraCurva(g,p);}
                }

            }else {

              for(int i=0;i<mi.length; i++) {
                  poly2.addPoint((int)mi[i][0], (int)mi[i][1]);
              }
              g.fillPolygon(poly2);

            }
            }
          }



          Ponto2D medio(Ponto2D p1, Ponto2D p2) {
              return new Ponto2D((p1.x + p2.x)/2,(p1.y + p2.y)/2);
          }

          void geraCurva(Graphics g, Ponto2D p0, Ponto2D p1, Ponto2D p2, Ponto2D p3) {
            int x0 = iX(p0.x), y0 = iY(p0.y), x3 = iX(p3.x), y3 = iY(p3.y);

              if (Math.abs(x0 - x3) <= 1 && Math.abs(y0 - y3) <=1) {
                  g.drawLine(x0, y0, x3, y3);
              } else {
              Ponto2D 
                  a =medio(p0, p1), b=medio(p3, p2), c= medio(p1,p2), 
                  a1=medio(a,c), b1=medio(b,c), c1=medio(a1,b1);
              geraCurva(g,p0,a,a1,c1);
              geraCurva(g,c1,b1,b,p3);
              }             

          }
          void geraCurva(Graphics g, Ponto2D[] p) {
              int m = 50, n = p.length;
              float xA, yA, xB, yB, xC, yC, xD, yD;
              float a0, a1, a2, a3, b0, b1, b2, b3;
              float x = 0, y =0, x0, y0;
              boolean primeiro = true;
              for (int i = 1; i < n-2; i++) {
                  xA = p[i-1].x; xB  = p[i].x; xC = p[i+1].x; xD = p[i+2].x;
                  yA = p[i-1].y; yB  = p[i].y; yC = p[i+1].y; yD = p[i+2].y;

                  a3 = (-xA + 3 * (xB - xC) + xD) / 6;
                  b3 = (-yA + 3 * (yB - yC) + yD) / 6;

                  a2 = (xA - 2 * xB + xC) / 2;
                  b2 = (yA - 2 * yB + yC) / 2;

                  a1 = (xC - xA) / 2;
                  b1 = (yC - yA) / 2;

                  a0 = (xA + 4 * xB + xC)/6;
                  b0 = (yA + 4 * yB + yC)/6;

                  for (int j=0; j<=m; j++) {
                      x0 = x;
                      y0 = y;
                      float t = (float) j / (float) m;
                      x = ((a3 * t + a2) * t + a1) * t + a0;
                      y = ((b3 * t + b2) * t + b1) * t + b0;
                      if (primeiro) primeiro = false;
                      else
                          g.drawLine(iX(x0),iY(y0),iX(x),iY(y));
                  }
              }
          }
          void limpar() {
            this.repaint();
          }
          void drawLine(Graphics g, float xP, float yP, float xQ, float yQ) {
            g.drawLine(iX(xP),iY(yP),iX(xQ), iY(yQ));
          }


          void initValues() {

            Dimension d = getSize();
              maxX = d.width - 1; maxY = d.height - 1;
              pixelSize = Math.max(rWidth / maxX, rHeight / maxY);
              centerX = maxX / 2; centerY = maxY / 2;          
          }

          void drawPoly(Graphics g, Poly poly) {
                  int n = poly.size();
                  if (n== 0) return;
                  Ponto2D p1 = poly.vertexAt(n - 1);
                  for (int i=0; i< n; i++) {
                      Ponto2D p2 = poly.vertexAt(i);
                      drawLine(g,p1.x, p1.y,p2.x, p2.y);
                      p1 = p2;
                  }


              }



              class Poly {
                  Vector<Ponto2D> vp = new Vector<Ponto2D>();

                  void addVertex(Ponto2D p) {vp.addElement(p);}

                   int size() {return vp.size();}   

                   Ponto2D vertexAt(int i) { return (Ponto2D) vp.elementAt(i);   }

                   void clipPoli(float xmin, float ymin, float xmax, float ymax) {
                      Poly poly1 = new Poly();
                      int n;
                      Ponto2D pi, pp;
                      boolean piIns, ppIns;

                      //lado do xmax
                      if ((n = size()) == 0) return;
                      pp = vertexAt(n - 1);
                      for (int i=0; i<n; i++) {
                          pi = pp; pp = vertexAt(i);
                          piIns = pi.x<=xmax;  ppIns = pp.x <= xmax; 
                          if (piIns != ppIns)
                              poly1.addVertex(new Ponto2D(xmax, 
                                      pi.y + (pp.y - pi.y) * (xmax - pi.x) / (pp.x - pi.x)));
                          if (ppIns) poly1.addVertex(pp);
                      }
                      vp = poly1.vp; poly1 = new Poly();

                      //lado do xmin
                      if ((n = size()) == 0) return;
                      pp = vertexAt(n-1);
                      for (int i=0; i<n; i++) {
                          pi = pp; pp = vertexAt(i);
                          piIns = pi.x>=xmin;  ppIns = pp.x >= xmin; 
                          if (piIns != ppIns)
                              poly1.addVertex(new Ponto2D(xmin, 
                                      pi.y + (pp.y - pi.y) * (xmin - pi.x) / (pp.x - pi.x)));
                          if (ppIns) poly1.addVertex(pp);
                      }
                      vp = poly1.vp; poly1 = new Poly();


                      //lado do ymax
                      if ((n = size()) == 0) return;
                      pp = vertexAt(n-1);
                      for (int i=0; i<n; i++) {
                          pi = pp; pp = vertexAt(i);
                          piIns = pi.y<=ymax;  ppIns = pp.y <= ymax; 
                          if (piIns != ppIns)
                              poly1.addVertex(new Ponto2D(pi.x + 
                                      (pp.x - pi.x) * (ymax - pi.y) / (pp.y- pi.y),ymax));
                          if (ppIns) poly1.addVertex(pp);
                      }
                      vp = poly1.vp; poly1 = new Poly();

                      //lado do ymin
                      if ((n = size()) == 0) return;
                      pp = vertexAt(n-1);
                      for (int i=0; i<n; i++) {
                          pi = pp; pp = vertexAt(i);
                          piIns = pi.y>=ymin;  ppIns = pp.y >= ymin; 
                          if (piIns != ppIns)
                              poly1.addVertex(new Ponto2D(pi.x + 
                                      (pp.x - pi.x) * (ymin - pi.y) / (pp.y- pi.y),ymin));
                          if (ppIns) poly1.addVertex(pp);
                      }
                      vp = poly1.vp; poly1 = new Poly();
                  }
              }

    } 
  }

class Ponto2D {
      float x, y;
      Ponto2D(float x, float y) {this.x= x; this.y = y;}
}
