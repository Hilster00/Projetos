package TrabalhoCG;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JToolBar;
import javax.swing.JComboBox;
import javax.swing.JDesktopPane;

public class Janela extends JFrame {
	int x0,x1,y0,y1,xf,yf,xmi,xma,ymi,yma;
	int mx,my;
	int cliques=0;
	int algoritmo[]= new int[2];
	public Janela(int altura,int largura) {
		
		sub_janela j = new sub_janela();
		janpol jj = new janpol();
		
		//configurando a janela
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(0, 0, 600, 600);
		//setBounds(0, 0, altura+16, largura+39);
		this.setResizable(false);
		
		JPanel panel = new JPanel();
		//panel.setBounds(0, 0, altura, largura);
		panel.setBounds(0, 0, 600, 600);
		getContentPane().add(panel);
		panel.setLayout(null);
		
		Desenha desenho = new Desenha(altura,largura); 
		panel.add(desenho);
		
		//Menu de barra
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
				
		//Primitivas
		JMenu Primitivas = new JMenu("Primitivas");
		menuBar.add(Primitivas);
				
		//Cores
		JMenu Cores = new JMenu("Cores");
		menuBar.add(Cores);
		Cores.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				j.mudar_visibilidade();
			}
		});
				
		//
		JMenu linhas = new JMenu("Linhas");
		Primitivas.add(linhas);
				//linhas	
					JMenu l1 = new JMenu("Analitico");
					JMenu l2 = new JMenu("DDA");
					JMenu l3 = new JMenu("Breseham");
					linhas.add(l1);
					linhas.add(l2);
					linhas.add(l3);
					l1.addMouseListener(new MouseAdapter() {
						@Override
						public void mouseClicked(MouseEvent e) {
							desenho.limpa();
							panel.repaint();
							algoritmo[0]=0;
							algoritmo[1]=0;
							cliques=0;
								
						}
					});	
					l2.addMouseListener(new MouseAdapter() {
						@Override
						public void mouseClicked(MouseEvent e) {
							desenho.limpa();
							panel.repaint();
							algoritmo[0]=0;
							algoritmo[1]=1;
							cliques=0;
						}
					});
					l3.addMouseListener(new MouseAdapter() {
						@Override
						public void mouseClicked(MouseEvent e) {
							desenho.limpa();
							panel.repaint();
							algoritmo[0]=0;
							algoritmo[1]=2;
							cliques=0;
						}
					});
				
		//
		JMenu poligonos = new JMenu("Poligonos");
		Primitivas.add(poligonos);
					

				JMenu p1 = new JMenu("Varredura");
				JMenu p2 = new JMenu("BoundaryFill");
				JMenu p3 = new JMenu("Análise Geométrica");
				poligonos.add(p1);
				poligonos.add(p2);
				poligonos.add(p3);
				
				p1.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						desenho.limpa();
						panel.repaint();
						
						algoritmo[0]=1;
						algoritmo[1]=0;
						jj.mudar_visibilidade();
						cliques=0;
					}
				});	
				p2.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						desenho.limpa();
						panel.repaint();
						algoritmo[0]=1;
						algoritmo[1]=1;
						jj.mudar_visibilidade();
						cliques=0;
					}
				});
				p3.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						desenho.limpa();
						panel.repaint();
						algoritmo[0]=1;
						algoritmo[1]=2;
						jj.mudar_visibilidade();
						cliques=0;
					}
				});
					
		//
		JMenu circulos = new JMenu("Circulos");
		Primitivas.add(circulos);
		
			JMenu c1 = new JMenu("Paramétrica");
			JMenu c2 = new JMenu("Incremental com Simétria");
			JMenu c3 = new JMenu("Breseham");
			circulos.add(c1);
			circulos.add(c2);
			circulos.add(c3);
			
			c1.addMouseListener(new MouseAdapter() {
				@Override
				public void mouseClicked(MouseEvent e) {
					desenho.limpa();
					panel.repaint();
					algoritmo[0]=2;
					algoritmo[1]=0;
					cliques=0;
				}
			});	
			c2.addMouseListener(new MouseAdapter() {
				@Override
				public void mouseClicked(MouseEvent e) {
					desenho.limpa();
					panel.repaint();
					algoritmo[0]=2;
					algoritmo[1]=1;
					cliques=0;
				}
			});
			c3.addMouseListener(new MouseAdapter() {
				@Override
				public void mouseClicked(MouseEvent e) {
					desenho.limpa();
					panel.repaint();
					algoritmo[0]=2;
					algoritmo[1]=2;
					cliques=0;
				}
			});
		
		setTitle("Trabalho CG");
		getContentPane().setLayout(null);
		this.setVisible(true);
		
		panel.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent clique) {
				Graphics g = getGraphics();
				g.setColor(new Color(j.cor[0], j.cor[1], j.cor[2]));
				
				x1=clique.getX();
				y1=clique.getY();

				if( algoritmo[0] == 0){
					if(cliques != 0) {
						if(x0>x1) {
							x0=x0+x1;
							x1=x0-x1;
							x0=x0-x1;
						}
						if(algoritmo[0] == 0) {
							desenho.algAnalitico(g, x0, y0+56, x1, y1+56);
						}else {
							if(algoritmo[1] == 1) {
								
								desenho.algDDA(g, x0, y0+56, x1, y1+56);
							}else {
								desenho.algBres(g, x0, y0, x1, y1);
							}
						}
						cliques=0;
					}else {
						cliques+=1;
						x0=x1;
						y0=y1;
					}
				}else {
					if(algoritmo[0] == 2) {
						if(algoritmo[1] == 0) {
							desenho.algParam(g, 100, x1, y1+56);
						}else {
							if(algoritmo[1] == 1) {
								desenho.algIncSem(g, 100, x1, y1+56);
							}else {
								desenho.algBresCir(g, 100, x1, y1+56);
							}
						}				
					}else {
						if (cliques < jj.quantidade) {
							if(cliques > 0) {
								desenho.algBres(g, x0, y0, x1, y1);
								if(x1<xmi) {
									xmi=x1;
								}else {
									if(xma<x1) {
										xma=x1;
									}
								}
								if(y1<ymi) {
									ymi=y1;
								}else {
									if(yma<y1) {
										yma=y1;
									}
								}
							}else {
								xf=x1;
								yf=y1;	
								xmi=xf;
								xma=xf;
								ymi=yf;
								yma=yf;
								mx=0;
								my=0;
							}
							cliques+=1;
							x0=x1;
							y0=y1;
							mx+=x1;
							my+=y1;
							if(cliques==jj.quantidade) {
								desenho.algBres(g, xf, yf, x1, y1);
								if(algoritmo[1] == 0) {
									desenho.preVarred(g,xmi, xmi, xma, yma);;
								}else {
									if(algoritmo[1] == 1) {
										mx=(int) mx /jj.quantidade;
										my=(int) my /jj.quantidade;
										desenho.preBF(g,mx, my);;
									}else {
										desenho.preAGeo(g);;
									}
								}
							}
						}
						
					}
				}
		
				
			}
		});
	}
}
