<template>
  <section class="container">
    <h3 class="mb-3">Контакты</h3>
    <h4 class="mb-3">Адрес</h4>
    <div class="row">
      <div class="col-md">
        <yandex-map
            class="v-map__mapping"
            zoom="17"
            style="width: 100%; max-width: 100%; height: 50vh;"
            :coords="coords"
        >
          <ymap-marker
              marker-type="placemark"
              :coords="coords"
              marker-id="123"
              :icon="markerIcon"
          />
        </yandex-map>
      </div>
      <div class="col-md">
        <h4 class="mb-3">Офис в городе Омск</h4>
        <h5>Адрес</h5>
        <p>644099, Омская обл, г Омск, Центральный округ, ул Ленина, д 10, каб. 12</p>
        <h5>Время работы</h5>
        <table class="table" style="font-size: small">
          <thead>
          <tr>
            <th scope="col">День недели</th>
            <th scope="col">Время работы</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <th scope="row">ПН</th>
            <td>10:00/20:00</td>
          </tr>
          <tr>
            <th scope="row">ВТ</th>
            <td>10:00/20:00</td>
          </tr>
          <tr>
            <th scope="row">СР</th>
            <td>10:00/20:00</td>
          </tr>
          <tr>
            <th scope="row">ЧТ</th>
            <td>10:00/20:00</td>
          </tr>
          <tr>
            <th scope="row">ПТ</th>
            <td>10:00/18:00</td>
          </tr>
          <tr>
            <th style="color:red" scope="row">СБ</th>
            <td>Офис не работает</td>
          </tr>
          <tr>
            <th style="color:red" scope="row">ВС</th>
            <td>Офис не работает</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <h4 class="my-3 ">Социальные сети</h4>
    <div class="row">
      <ul class="social-icons icon-circle list-unstyled list-inline">
        <li>
          <a href="#"><i class="fa fa-phone"></i>  +7(999)456-45-74</a>
        </li>
        <li class="d-flex justify-content-end">
          <a href="#">danucha129@gmail.com  <i class="fa fa-envelope"></i></a>
        </li>
        <li >
          <a href="#"><i class="fa fa-brands fa-vk"></i>  Группа Вконтакте</a>
        </li>
        <li class="d-flex justify-content-end">
          <a href="#">Страница в Instagram  <i class="fa fa-brands fa-instagram"></i></a>
        </li>
        <li>
          <a href="#"><i class="fa fa-brands fa-telegram"></i>  Канал в Telegram</a>
        </li>
        <li class="d-flex justify-content-end">
          <a href="#">+7(999)456-45-74  <i class="fa fa-brands fa-whatsapp"></i></a>
        </li>
        <li>
          <a href="https://github.com/EeVakEn"><i class="fa fa-brands fa-github"></i>  Github разработчика</a>
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
import {yandexMap, ymapMarker} from "vue-yandex-maps";

export default {
  name: "contacts",
  components: {yandexMap, ymapMarker},
  data() {
    return {
      coords: [54.986887, 73.372869],
      markerIcon: {
        content: 'yourwear',
        contentLayout: '<div style="background: black; width: 50px; color: #FFFFFF; font-weight: bold;">{{content}}</div>'
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.list-inline li {
  padding-right: 5px;
  padding-left: 5px;
  margin-bottom: 10px;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}

/*Change icons size here*/
.social-icons .fa {
  font-size: 22px;
}

/*Change icons circle size and color here*/
.social-icons .fa {
  width: 40px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  color: #FFF;
  transition: all 0.3s ease-in-out;
}

.social-icons.icon-circle .fa {
  border-radius: 50%;
}

.social-icons .fa:hover, .social-icons .fa:active {
  color: #FFF;
  box-shadow: 1px 1px 3px #333;
}

.social-icons .fa:hover, .social-icons .fa:active {
  transform: scale(1.02);
}

.social-icons .fa {
  background-color: $dark-color;
}

.social-icons .fa-github, .social-icons .fa-github-alt, .social-icons .fa-github-square {
  background-color: #070709;
}

.social-icons .fa-instagram {
  background-color: #E4405F;
}

.social-icons .fa-vk {
  background-color: #4C75A3;
}

.social-icons .fa-telegram {
  background-color: #0099FF;
}

.social-icons .fa-whatsapp {
  background-color: #25D366;
}

.social-icons .fa-youtube, .social-icons .fa-youtube-play, .social-icons .fa-youtube-square {
  background-color: #CD201F;
}

</style>