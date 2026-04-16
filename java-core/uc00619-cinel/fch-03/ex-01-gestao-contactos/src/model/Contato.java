package model;

public class Contato {

    private String nome;
    private String telefone;
    private String email;
    private String grupo;

    public Contato(String nome, String telefone, String email, String grupo) {
        this.nome = nome;
        this.telefone = telefone;
        this.email = email;
        this.grupo = grupo;
    }

    public String toFileString() {
        return nome + ";" + telefone + ";" + email + ";" + grupo;
    }

    public String getNome() { return nome; }
    public String getTelefone() { return telefone; }
    public String getEmail() { return email; }
    public String getGrupo() { return grupo; }
}