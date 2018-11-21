package com.bigdata.model.UserBehavior;


import java.util.Date;

public class Value {

    protected Integer id;

    protected String username;

    protected String type;

    protected String text;

    protected Date timestamp;


    public Value() {
    }

    public Value(String username, String type, String text, Date timestamp) {
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
