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

public class sub_janela extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JButton btnNewButton;

	int cor[] = new int[3];
	boolean visivel=false;
	public sub_janela() {
		
		cor[0] = 255;
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(0, 0, 215, 114);
		this.setResizable(false);
		
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		textField = new JTextField();
		textField.setText("255");
		textField.setBounds(5, 10, 60, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setText("0");
		textField_1.setBounds(70, 10, 60, 20);
		contentPane.add(textField_1);
		textField_1.setColumns(10);
		
		textField_2 = new JTextField();
		textField_2.setText("0");
		textField_2.setBounds(135, 10, 60, 20);
		contentPane.add(textField_2);
		textField_2.setColumns(10);
		
		btnNewButton = new JButton("Confirmar");
		btnNewButton.setBounds(51, 41, 89, 23);
		contentPane.add(btnNewButton);
		
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				cor[0] = Integer.parseInt(textField.getText());
				cor[1] = Integer.parseInt(textField_1.getText());
				cor[2] = Integer.parseInt(textField_2.getText());
				if(cor[0] < 0 || cor[0] > 255) {
					textField.setText("255");
					cor[0]=255;
				}
				if(cor[1] < 0 || cor[1] > 255) {
					textField_1.setText("255");
					cor[1]=255;
				}
				if(cor[2] < 0 || cor[2] > 255) {
					textField_2.setText("255");
					cor[2]=255;
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
