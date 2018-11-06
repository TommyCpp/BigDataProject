package com.bigdata.model.UserBehavior;


import javax.persistence.*;
import java.util.Date;

@Entity
public class Behavior {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;

    private String username;

    private String type;

    private String text;

    private Date timestamp;


    public Behavior() {
    }

    public Behavior(String username, String type, String text, Date timestamp) {
        this.username = username;
        this.type = type;
        this.text = text;
        this.timestamp = timestamp;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Date getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(Date timestamp) {
        this.timestamp = timestamp;
    }
}
