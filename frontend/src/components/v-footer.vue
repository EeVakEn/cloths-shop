<template>
  <footer class="site-footer">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6">
          <h6>О сайте</h6>
          <p class="text-justify">Yourwear — место, в котором ты сможешь найти стильную, удобную, качественную и
            приятную одежду для себя и в подарок своим близким по низким ценам с доставкой во всей России. <br>
          <b>Сайт является выпускной квалификационной работой студента группы ИВТ-183 Омского государственного технического университета <br>
            Ивахина Данила Евгеньевича</b> <br>
            <b>САЙТ НЕ ЯВЛЯЕТСЯ КОММЕРЧИСКИМ<br>ТОЛЬКО ДЛЯ ДЕМОСТРАЦИОННЫХ ЦЕЛЕЙ</b>
          </p>
        </div>

        <div class="col-xs-6 col-md-3">
          <h6>Категории</h6>
          <ul class="footer-links">
            <li><router-link to="/category/muzhskoe" replace>Мужское</router-link></li>
            <li><router-link to="/category/zhenskoe" replace>Женское</router-link></li>
          </ul>
        </div>

        <div class="col-xs-6 col-md-3">
          <h6>Навигация</h6>
          <ul class="footer-links">
            <li><router-link to="/" replace>Каталог</router-link></li>
            <li><router-link to="cart" replace>Корзина</router-link></li>
            <li><router-link to="favorites" replace>Избранное</router-link></li>
            <li><router-link to="account" replace>Личный кабинет</router-link></li>
            <li><router-link to="about" replace>О нас</router-link></li>
            <li><router-link to="contacts" replace>Контакты</router-link></li>
          </ul>
        </div>
      </div>
      <hr>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 col-sm-6 col-xs-12">
          <p class="copyright-text">Copyright &copy; 2022 All Rights Reserved by
            <a class="link" style="color: #F5F5F5 !important;" href="https://github.com/EeVakEn">Danil Ivakhin</a>.
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "v-footer",
}
</script>

<style lang="scss" scoped>
.site-footer {
  background-color: $dark-color;
  padding: 45px 0 20px;
  font-size: 15px;
  line-height: 24px;
  color: #737373;
}

.site-footer hr {
  border-top-color: #bbb;
  opacity: 0.5
}

.site-footer hr.small {
  margin: 20px 0
}

.site-footer h6 {
  color: #fff;
  font-size: 16px;
  text-transform: uppercase;
  margin-top: 5px;
  letter-spacing: 2px
}

.site-footer a:hover {
  color: #3366cc;
  text-decoration: none;
}

.footer-links {
  padding-left: 0;
  list-style: none
}

.footer-links li {
  display: block
}

.footer-links li a {
  color: #737373 !important;
}

.footer-links a:active, .footer-links a:focus, .footer-links a:hover {
  color: #3366cc;
  text-decoration: none;
}

.footer-links.inline li {
  display: inline-block
}

.site-footer .social-icons {
  text-align: right
}

.site-footer .social-icons a {
  width: 40px;
  height: 40px;
  line-height: 40px;
  margin-left: 6px;
  margin-right: 0;
  border-radius: 100%;
  background-color: #33353d
}

.copyright-text {
  margin: 0
}
</style>