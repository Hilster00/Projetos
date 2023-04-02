package TrabalhoCG;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import java.awt.Color;
import java.awt.Component;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JToolBar;

import TrabalhoCG.Recorte.RecLinhas;

import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JDesktopPane;

public class Janela extends JFrame {
	int opcoes[]= new int[2];
	public Janela(int altura,int largura) {
		
		
		//configurando a janela
		this.setTitle("Algoritmo de Recorte de Retas de Cohen-Sutherland");
	    this.setSize(600,600);
	    RecLinhas desenho = new RecLinhas();
	    this.add("Center",desenho);
	    this.setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
	    this.setLocationRelativeTo(null);
	    this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	    this.setVisible(true);
	    
		//setBounds(0, 0, altura+16, largura+39);
		this.setResizable(false);
		
		
		JPanel panel = new JPanel();
		//panel.setBounds(0, 0, altura, largura);
		panel.setBounds(0, 0, 600, 600);
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
							opcoes[0]=0;
							opcoes[1]=0;
							desenho.repaint();
							mudar_cursor(1); 
							desenho.setVisible(true);
						}
					});	
					r2.addMouseListener(new MouseAdapter() {
						@Override
						public void mouseClicked(MouseEvent e) {
							opcoes[0]=0;
							opcoes[1]=1;
							mudar_cursor(1);
							desenho.setVisible(false);
						}
					});
					
				
		//
		JMenu curvas = new JMenu("Curvas");
		menuBar.add(curvas);
					

				JMenu c1 = new JMenu("Bézier");
				JMenu c2 = new JMenu("B-Spilner");

				curvas.add(c1);
				curvas.add(c2);
				
				c1.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						opcoes[0]=1;
						opcoes[1]=0;
						mudar_cursor(0);
						panel.repaint();
					}
				});	
				c2.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						opcoes[0]=1;
						opcoes[1]=1;
						mudar_cursor(0);
						panel.repaint();
					}
				});
				
					
		//
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
					opcoes[0]=2;
					opcoes[1]=0;
					mudar_cursor(0);
					panel.repaint();
				}
			});	
			t2.addMouseListener(new MouseAdapter() {
				@Override
				public void mouseClicked(MouseEvent e) {
					opcoes[0]=2;
					opcoes[1]=1;
					mudar_cursor(0);
					panel.repaint();
				}
			});
			t3.addMouseListener(new MouseAdapter() {
				@Override
				public void mouseClicked(MouseEvent e) {
					opcoes[0]=2;
					opcoes[1]=2;
					mudar_cursor(0);
					panel.repaint();
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
				
				
		setTitle("Trabalho CG");
		getContentPane().setLayout(null);
		this.setVisible(true);

		

		
		panel.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent clique) {
				
			}	
		});

	      
	}
	void mudar_cursor(int i) {
		if(i == 1) {
			this.setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
		}else {
			setCursor(Cursor.getDefaultCursor());

		}
		
	}
	class RecLinhas extends JComponent {
        float xmin, xmax, ymin, ymax, rWidth = 10.0F, rHeight = 7.5F, pixelSize;
        int maxX, maxY, centerX, centerY, np=0;

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
        
        public RecLinhas() {
            addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent evt) {
            	if(opcoes[0]==opcoes[1] && opcoes[0] == 0) {
	            		
	            	
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
	                repaint();
                }
            }
        });
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
        
        void initValues() {
        Dimension d = getSize();
        maxX = d.width - 1; maxY = d.height - 1;
        pixelSize = Math.max(rWidth / maxX, rHeight / maxY);
        centerX = maxX / 2; centerY = maxY / 2;
        }
    
        @Override
        public void paint (Graphics g) {
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
        
        }
        void limpar() {
        	this.repaint();
        }
        void drawLine(Graphics g, float xP, float yP, float xQ, float yQ) {
            g.drawLine(iX(xP),iY(yP),iX(xQ), iY(yQ));
        }
}   
}
