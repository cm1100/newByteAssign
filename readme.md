# Url Managing System

### ARCHITECTURE
#### Just a simple table containing hashed url with its usage limit and used count

### COMPILE PROJECT
    git clone https://github.com/cm1100/newByteAssign.git
    cd newByteAssign
    bash build.sh


### STARTUP THE PROJECT
    source venv/bin/activate
    python manage.py runserver

### MAIN APIS
    
    WORKING :- To hash a url
    POST :- http://127.0.0.1:8000/url_manager/url_detail/
    PAYLOAD :- {
    "url":"https://apiuat.igrow.ag/api/v1/usermngmnt/mo_dashboard/list_mos",
    "use_limit":2
    }
    # use_limit should not be sent for unlimited usage

    WORKING :- To get a url from hash
    GET:- http://127.0.0.1:8000/url_manager/url_detail/get_by_hash/5182951440770647301


### SWAGGER CAN BE SEEN FROM
    http://127.0.0.1:8000/swagger/


### TESTS CAN BE RUN USING
    python manage.py test