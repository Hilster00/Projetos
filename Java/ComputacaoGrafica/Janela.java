package TrabalhoCG;

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

        this.add(new Desenha());
    }

}
