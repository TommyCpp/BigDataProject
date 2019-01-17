package com.bigdata.model.UserGoogleZip;


import javax.persistence.*;

@Entity
public class UserActivity {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    @Column(length = 1000)
    protected Integer id;
    protected String type = null;

    @Lob
    @Column(columnDefinition="text")
    protected String link = null;

    protected String time = null;

    @Lob
    @Column(columnDefinition="text")
    protected String content = null;

    @Lob
    @Column(columnDefinition="text")
    protected String last_link = null;

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getLast_link() {
        return last_link;
    }

    public void setLast_link(String last_link) {
        this.last_link = last_link;
    }
}
