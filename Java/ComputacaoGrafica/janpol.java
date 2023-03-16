package TrabalhoCG;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;

public class janpol extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	int quantidade=3;
	boolean visivel=false;
	
	public janpol() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 340, 110);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		textField = new JTextField();
		textField.setText("3");
		textField.setBounds(10, 11, 304, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		JButton btnNewButton = new JButton("Salvar");
		btnNewButton.setBounds(10, 42, 89, 23);
		contentPane.add(btnNewButton);
		
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				quantidade = Integer.parseInt(textField.getText());
				if(quantidade < 3) {
					textField.setText("3");
					quantidade=3;
				}
				mudar_visibilidade();
			}

		});
		
	}
	public void mudar_visibilidade() {
		visivel=!(visivel);
		this.setVisible(visivel);
	}
}
