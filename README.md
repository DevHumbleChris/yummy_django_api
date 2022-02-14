# YUMMY DJANGO API

Yummy Django API, it's the exclusive API used for the [e-yummy-ke](https://e-yummy-ke.web.app) vue web app .

## Technologies Used:
1. Python.
2. Django.
3. django-cors-headers.
4. djoser.
5. djangorestframework

----------

## API ROUTES.

Web URL: [https://e-yummy-ke-api.herokuapp](https://e-yummy-ke.herokuapp.com)

Home Route.
> ALLOWED METHODS: GET, POST

'''
/
'''

Category Route.
> ALLOWED METHODS: GET, POST

'''
api/v1/category/
'''

Home Route.
> ALLOWED METHODS: GET

'''
/api/v1/all-products/
'''

Create Product Route.
> ALLOWED METHODS: POST

'''
/api/v1/create-product/
'''

Route for getting all Products of a Specific Category.
> ALLOWED METHODS: GET

'''
api/v1/category/<str:category_name>/products/
'''
