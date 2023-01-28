# Beyond Real Estate
### Property Management App

https://user-images.githubusercontent.com/99300376/215223334-4ee32207-fb6f-408e-9cf7-298050cc3c94.mp4

Beyond Real Estate is a full-stack property management application built on Python, Flask, SQL, Bootstrap and Google Map API. The intention behind this project was to create a "one-stop shop" software application than can help owners, property managers and/or real estate professionals to organize all the properties and tenants under their care.

The idea for this project came from my experience as a real estate agent, when clients would ask me to help assist them with managing their properties. At that time, I did not know of any software that I could recommend to my clients. As I learned more about different coding languages, frameworks and as my coding skills improved; I thought this would be a great opportunity to combine and showcase my skills as a software devloper and former real estate agent.

# Technologies Used
Beyond Real Estate is built on Python, SQL, Flask, Google API, and Bootstrap. 

<img src='https://user-images.githubusercontent.com/99300376/215221527-05afec60-aa4d-4f0f-8109-215eaa4d6326.png' width='50'/><img src='https://user-images.githubusercontent.com/99300376/215221547-85726751-cc34-4aa6-9ad4-3696d2b55d06.png' width='50'/>
<img src='https://user-images.githubusercontent.com/99300376/215221562-5a3ed772-2f0c-4e80-8abe-85d466f2506f.png' width='50'/>
<img src='https://user-images.githubusercontent.com/99300376/215221599-13fefde9-6ced-4805-a8c4-47b3992fe92b.png' width='50'/>

# Features and Highlights

* [Landing Page](#examples)
  - [Login/Registration](#Login/Registration)
  - [Full CRUD for registered users](#FullCRUDforregisteredusers)
  - [Google Maps API](#GoogleMapsApi)
  - [What I've Learned](#WhatIveLearned)
  - [Next Steps](#nextSteps)

<a name='Login/Registration'></a>
## Login/Registration
<img src='https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/f7e577ad-d4df-4ca0-b6c8-39ce044a65b6.gif?ClientID=vimeo-core-prod&Date=1674861993&Signature=4bf2db069af27bf73da15b1352a5ee2cdea1a278' width='600'/>

In order to use the application users must first create an account to access all of the features. JQuery was used to add the toggle functionality to switch between the login form and the registration form. The passwords are encrypted using bcrypt and stored in the database using SQL.  

<a name='FullCRUDforregisteredusers'></a>
## Full CRUD for registered users
<img src='https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/015e0075-c9ce-4371-b785-a24e04cbcb16.gif?ClientID=vimeo-core-prod&Date=1674862329&Signature=12a8a5d97042c28e08853914b31b6117f85d05bb' width='600'/>

Registered users have access to full CRUD features for their properties, tenants, and vendors. Registered users can create, edit and delete the properties, tenants, and vendors in their profile. They are able to update information that is related to what they need and they can also upload pictures. For example, users can edit whether a property is vacant or occupied; the changes with be visible in the overall properties view too.

<a name='GoogleMapsApi'></a>
## Google Maps API
<img src='https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/ea307459-4e25-4769-8e3a-46c1ec8e54d1.gif?ClientID=vimeo-core-prod&Date=1674862149&Signature=820e436ad0395b1f3d287b9171b2e3c6fcbe6abd' width='600' />

This application used the Google API to render that map and geolocation to create the markers for the properties that are being managed by the user. Users can toggle between a list view or a map view of the properties under their care. In the map view, they can see where each property is on the map.

<a name='WhatIveLearned'></a>
## What I've Learned

This project gave me the opportunity to apply and demonstrate what I have learned in:

creating a database to seamlessly and coherently connect data
setting up a backend server with user authentication, error handling, and API routes following RESTful conventions
designing a frontend application with html, css bootsrap and using Flask to connect to the backend

This project also allowed me to explore:
- Learning how to integrate an external API (Google Maps) 
- Handling user authentification with bcrypt.

<a name='nextSteps'></a>
## Next Steps

- Create a profile page for each property. The profile will have all the information that pertains to that particular property, like the tenants assigned to it, any necessary documents, and more. 
- Implement image and document uploads using AWS S3. (v1.0.1)
- Search for the properties on the map using its address. 
- Media queries to make the design more responsive to different sized screens, as well as a mobile-friendly (v1.0.1)
