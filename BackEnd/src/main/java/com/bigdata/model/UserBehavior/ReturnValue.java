package com.bigdata.model.UserBehavior;

public class ReturnValue {
    int id;
    String error="0";
    String type;
    Behavior value;

    public ReturnValue() {
    }

    public ReturnValue(int id, String type, Behavior value) {
        this.id = id;
        this.type = type;
        this.value = value;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Behavior getValue() {
        return value;
    }

    public void setValue(Behavior value) {
        this.value = value;
    }

    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }
}
