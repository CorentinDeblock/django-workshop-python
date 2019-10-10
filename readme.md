# Workshop amelioration de mon côté

Voila la version finale que j'ai fait cette nuit, elle est pas optimale mais je pense que elle fera l'affaire.

N'hésitez pas retirer des modification que vous jugez inutile.

En attendant voici une doc des modification: 

## Le model post a été changer (gellery/models.py)

Les modification apporter sont mineure mais permet de trier par ordre de date dans les views et permet d'enregistrer des votes.

Avant:

```
from django.db import models

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
```

Après:

```
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
```

## Des views on été rajouté et la post a été un peu modifier

Les modifications permettent d'ordonner les posts par les dates et d'ajouter un système sur les views like et dislike

get_object_or_404: permet de retouner un object dans le model ou 404</br>
-created_at: Permet d'ordonner le post de manière décroissante par rapport a la date

Avant:

```
from django.views import generic
from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post
// Create your views here.

class index(generic.ListView):
    model = Post
    template_name="pages/index.html"

class CreatePostView(generic.CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'pages/post.html'
    success_url = reverse_lazy('gallery:index')
```

Après:

```
from django.shortcuts import redirect,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post

class index(generic.ListView):
    model = Post
    template_name="pages/index.html"
    ordering=['-created_at']

class CreatePostView(generic.CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'pages/post.html'
    success_url = reverse_lazy('gallery:index')

def like(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    like = post.like + 1
    Post.objects.filter(pk=post_id).update(like=like)
    return redirect("/")

def dislike(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    dislike = post.dislike + 1
    Post.objects.filter(pk=post_id).update(dislike=dislike)
    return redirect("/")
```

## Des views on été rajouté et la post a été un peu modifier

Juste une modification de structure de l'html pour pouvoir mieux trier en css avec grid et grid-template</br>
J'ai aussi ajouter une classe gallery pour pouvoir dissocier content et les images</br>
J'ai retirer l'ul et les li pour mettre une div ce qui me semblait plus simple a représenter visuellement et plus simple a stylisé.</br>
J'ai également ajouter les buttons like et dislike.

Avant:

```

{% block content %}
<ul>

  {% for post in object_list %}

  <li>

    <a href="#">
    <img src="{{ post.cover.url}}" alt="{{ post.title }}">
    </a>

    <h2>{{ post.title }}</h2>
  </li>

  {% endfor %}
</ul>


{% endblock %}
```

Après:

```
{% block content %}
  <div class="gallery">
    {% for post in object_list %}
    <div class="mb-3">
      <a class="image"href="#">
        <img src="{{ post.cover.url}}" alt="{{ post.title }}">
        </a>
    
        <h2>{{ post.title }}</h2>
        <div class="vote">
          <a class="far like fa-thumbs-up" href="{% url 'gallery:like' post.id %}"><span>{{ post.like }}</span></a>
          <a class="far dislike fa-thumbs-down" href="{% url 'gallery:dislike' post.id %}"><span>{{ post.dislike }}</span></a>
        </div>
    </div>
    {% endfor %}
  </div>
{% endblock %}

```

## Changement du style

Ajout de la classe gallery et d'un grid sur la gallery qui est mieux que le display flex.</br>
La grid est reponsive est responsive</br>
Ajout d'une stylisation sur les input et sur le bouton submit

Avant:

```
body {
    background: #f7c873;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #434343;
}

.logo {
    height: 350px;
    align-self: center;
}

.logo img {
    height: 100%;
}

.content {
    width: 80%;
    display: flex;
    justify-content: center;
    overflow: hidden;
   
}

.content ul {
  
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    justify-content: space-between;
    padding-left: 0;
    list-style-type: none;
}

.content ul li {
    display: flex;
    flex-direction: column;
    margin: 10px;
    height: 250px;
    width: 250px;
   
}

.content ul li a {
    height: 200px;
    overflow: hidden;
}

.content ul img {
    width: 100%;
    border-radius: 5px;
}

.content ul h2 {

    text-align: center;
    border-bottom: 3px groove rgba(67,67,67,0.2); 
    padding-bottom: 5px;
    
}

.photoAdd {
    position: absolute;
    right: 20px;
    top: 20px;
    height: 70px;
    width: 70px;
}

.photoAdd img {
    width: 100%;
    height: 100%;
}

form {
    border: 5px solid  rgba(67,67,67,0.5); 
    text-align: center;
    padding: 20px;
    width: 90%;
}

footer {
    position: absolute;
    bottom: 0;
}

#id_title {
    height: 20px;
}

```

Après:

```
body {
    background: #f7c873;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #434343;
}

.logo {
    height: 350px;
    align-self: center;
}

.logo img {
    height: 100%;
}
button {
    font-weight: bold;
    background-color:black;
    color:white;
    padding: 2px 10px;
    border:none;
    box-shadow: 0px 0px 3px 0px white;
    border-radius: 10px;
    transition: background-color 0.3s ease-in,color 0.3s ease-in,box-shadow 0.3s ease-in;
    cursor: pointer;
}
button:hover {
    background-color:white;
    color:black;
    box-shadow: 0px 0px 5px 1px black;
}
.content {
    width: 80%;
}
input[type='file'] {
    width:0.1px;
    height: 0.1px;
    position: absolute;
    overflow: hidden;
}
label[for='id_cover'] {
    background-color:#434343;
    padding: 5px 40px;
    color:white;
    border-radius: 5px;
    cursor:pointer; 
}
.gallery {
    display:grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-column-gap: 30px;
}
.gallery img {
    width: 100%;
    border-radius: 5px;
    height: 10vw;
}

.gallery ul h2 {

    text-align: center;
    border-bottom: 3px groove rgba(67,67,67,0.2); 
    padding-bottom: 5px;
    
}

.photoAdd {
    position: absolute;
    right: 20px;
    top: 20px;
    height: 70px;
    width: 70px;
}

.photoAdd img {
    width: 100%;
    height: 100%;
}
.gallery h2{
    text-align: center;
    border-bottom: 3px groove rgba(67,67,67,0.2); 
    padding-bottom: 5px;
}
.vote a {
    margin-left:5px;
    text-decoration: none;
    color:black
}
.vote .like:hover {
    color: blue;
}
.vote .dislike:hover {
    color: red;
}
.vote span {
    margin-left:2px;
}
form {
    border: 5px solid  rgba(67,67,67,0.5); 
    text-align: center;
    padding: 20px;
    width: 90%;
}

footer {
    position: absolute;
    bottom: 0;
}

.mb-3{
    margin-bottom:30px
}

#id_title {
    height: 20px;
}

@media screen and (max-width:900px){
    .gallery {
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr  !important;
    }
}

@media screen and (max-width:1300px){
    .gallery {
        grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr;
    }
}
@media screen and (max-width:600px){
    .gallery {
        grid-template-columns: 1fr 1fr  !important;
    }
    .gallery img {
        height: 25vw;
    }
}
@media screen and (max-width:300px){
    .gallery {
        grid-template-columns:1fr  !important;
    }
    .gallery img {
        height: 55vw;
    }
}
```