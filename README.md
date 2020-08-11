# Integrate Django and Vue.js

This is the Django + Vue.js project


Open `frontend` directory, install the Node dependencies, build the Vue.js application, and run the Vue dev server. 

```bash
cd frontend
npm install
npm build
npm serve
```

Finally, run the Django development server in a different terminal:

```bash
python manage.py runserver
```

Now you can view the production Vue application at `127.0.0.1:8000`, and the development application at `localhost:8080`. Both will use the local Django instance as the API.

Thanks for visiting!
