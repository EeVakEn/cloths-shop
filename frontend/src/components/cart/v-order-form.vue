<template>
  <div class="order-form container-fluid">
    <form class="row g-3" @submit.prevent="checkout">
      <h2>Оформление</h2>
      <section class="customer">
        <h3><i class="bi bi-person"/> Покупатель </h3>
        <router-link class="link" to="/log-in">Войти или зарегистрироваться</router-link>
        <hr/>
        <div class="row">
          <div class="col-md-6 my-2">
            <label for="firstname" class="form-label">Имя</label>
            <input type="text" v-model="firstname" class="form-control" id="firstname" required>
            <div v-if="$v.firstname.$dirty && $v.firstname.$invalid" class="invalid_feedback">
              Обязательное поле
            </div>
          </div>
          <div class="col-md-6 my-2">
            <label for="lastname" class="form-label">Фамилия</label>
            <input type="text" v-model="lastname" class="form-control" id="lastname" required>
            <div v-if="$v.lastname.$dirty && $v.lastname.$invalid" class="invalid_feedback">
              Обязательное поле
            </div>
          </div>
          <div class="col-md-6 my-2">
            <label for="phone" class="form-label">Телефон</label>
            <input type="text" v-model="phone" class="form-control" id="phone" maxlength="16" required>
            <div v-if="$v.phone.$dirty && $v.phone.$invalid" class="invalid_feedback">
              Некорректный номер
            </div>
          </div>
          <div class="col-md-6 my-2">
            <label for="email" class="form-label">Email</label>
            <input type="email" v-model="email" class="form-control" id="email" required>
            <div v-if="$v.email.$dirty && $v.email.$invalid" class="invalid_feedback">
              Некорректный адрес электронной почты.
            </div>
            <small>Для получения информации о заказе и связи</small>
          </div>
        </div>

      </section>
      <section class="delivery">
        <h3><i class="bi bi-truck"/> Доставка</h3>
        <hr/>
        <div class="row">

          <div class="col-md-12 my-2">
            <label for="city">Город</label>
            <dadata-suggestions
                class="form-control"
                style="padding: 0.375rem 0.75rem !important;"
                v-model="city"
                id="city"
                fieldValue="value"
                :fullInfo.sync="cityfull"
                :options="cityOptions"
            />
            <small>Например: г Омск</small>
          </div>


        </div>


        <div v-if="city.length" class="delivery_select">
          <h5>Выберите способ доставки</h5>
          <div class="raw">
            <label class="card-radio-btn">
              <input type="radio" name="demo" class="card-input-element d-none" value="курьер" v-model="deliveryType">
              <div class="card card-body">
                <div class="content_head">Курьер СДЭК</div>
                <div class="content_sub">Курьер доставит товар прям к двери. Только укажите корректный адрес.</div>
              </div>
            </label>
            <label class="card-radio-btn">
              <input type="radio" name="demo" class="card-input-element d-none" value="постамат"
                     v-model="deliveryType">
              <div class="card card-body">
                <div class="content_head">Постамат СДЭК</div>
                <div class="content_sub">Выберите ближайшую точку, откуда заберете товар.</div>
              </div>
            </label>
          </div>
        </div>


        <div v-if="deliveryType==='постамат'">
          <yandex-map
              class="v-map__mapping"
              zoom="13"
              style="width: 100%; max-width: 100%; height: 50vh;"
              :coords="coords"
          >
            <ymap-marker
                v-for="(mark, index) in surfaces"
                :key="index"
                :marker-id="index"
                marker-type="placemark"
                :coords="[mark.coordY, mark.coordX]"
                @balloonopen="bindListener(mark)"
                @balloonclose="unbindListener"
            >
              <div slot="balloon">
                <h4>{{ mark.code }}</h4>
                <div class="row">
                  <div v-if="mark.officeImageList" class="col">
                    <img style="width: 100%;" :src="mark.officeImageList[0].url">
                  </div>
                  <div class="col">
                    <div><strong>Название</strong>:{{ mark.name }}</div>
                    <div><strong>Адрес</strong>: {{ mark.fullAddress }}</div>
                    <div><strong>Время работы</strong>: {{ mark.workTime }}</div>
                    <button type="button" class="dark-button" id="btn_choose">Выбрать</button>
                  </div>
                </div>
              </div>
            </ymap-marker>

          </yandex-map>
        </div>

        <div v-if="deliveryType==='курьер'" class="row">
          <div class="col-md-6 my-2">
            <label for="street">Улица и дом</label>
            <dadata-suggestions
                class="form-control"
                style="padding: 0.375rem 0.75rem !important;"
                id="street"
                :fullInfo.sync="addressfull"
                field-value="value"
                :options="streetOptions"
            />
            <small>Например: ул Ленина</small>
          </div>

          <div class="col-md-6 my-2">
            <label for="room">Квартира</label>
            <input class="form-control" v-model.trim="room" id="room"/>
            <small>Оставьте пустым, если нет номера квартиры</small>
          </div>
        </div>
        <div v-if="$v.address_str.$dirty && $v.address_str.$invalid" class="invalid_feedback">
          Задайте корректный адрес доставки
        </div>

        <div v-if="address_str">
          <div class="card my-4">
            <div class="card-body">
              <h5 class="card-title">Информация о доставке</h5>
              <h6 class="card-subtitle mt-3">Тип доставки</h6>
              <p class="card-text">{{ deliveryType }}</p>
              <h6 class="card-subtitle ">Адрес доставки</h6>
              <p class="card-text text-justify">{{ address_str }}</p>
              <p v-if="deliveryType==='курьер'" class="card-subtitle sticky-right text-muted"><b>Стоимость доставки</b>:
                {{ courier_cost }} руб.</p>
              <p v-else class="card-subtitle sticky-right text-muted"><b>Стоимость доставки</b>: <span
                  style="color: #00cc66">бесплатно</span></p>
            </div>
          </div>
        </div>
      </section>
      <button class="dark-button mb-5" type="submit" style="width: 100%">Оформить заказ</button>
    </form>
  </div>
</template>

<script>
import IMask from 'imask' // чтобы задать маску для номера телефона
import {yandexMap, ymapMarker} from "vue-yandex-maps";
import axios from "axios";
import {validationMixin} from 'vuelidate'
import {required, email, minLength} from 'vuelidate/lib/validators'

export default {
  name: "v-order-form",
  components: {yandexMap, ymapMarker},
  mixins: [validationMixin],
  props: ['cost'],
  data() {
    return {

      coords: [55.751244, 37.618423],
      surfaces: [],
      firstname: "",
      lastname: "",
      phone: "",
      email: "",

      city: "",

      room: "",

      postamat: {},
      courier_cost: 250,
      dadata_city: {},
      dadata_address: {},

      deliveryType: '',

      cityfull: {},
      addressfull: {},

      cityOptions: {
        bounds: "city",
        floating: false,
        count: 5,
      },
      streetOptions: {
        bounds: "street-house",
        count: 5,
      },
      mask: '',
      mark: {},
      selectedMark: {},

    };
  },
  watch: {
    cityfull: function (val) {
      if (val) {
        this.dadata_city = val.data
        this.coords = [val.data.geo_lat, val.data.geo_lon]
        this.getAllPoints()
      }
    },
    addressfull: function (val) {
      if (val) {
        this.dadata_address = val
      }
    },


  },
  computed: {
    address_str: function () {
      if (this.deliveryType === 'курьер') {
        if (this.dadata_address) {
          let str = this.dadata_address.unrestricted_value
          if (this.room !== '') {
            str += ', кв. ' + this.room
          }
          return str
        } else return ''
      } else {
        if (this.selectedMark)
          return this.selectedMark.fullAddress
        else
          return ''
      }
    }
  },
  methods: {

    async checkout() {
      this.$v.$touch()
      if (!this.$v.$error) {
        this.$store.commit('SET_IS_LOADING', true)
        console.log('Валидация прошла успешно')
        let items = []
        this.$store.state.cart.forEach(item =>
            items.push({'product': item.variant_id, 'quantity': item.quantity})
        );
        const formData = {
          'firstname': this.firstname,
          'lastname': this.lastname,
          'email': this.email,
          'phone': this.phone,
          'address': this.address_str,
          'delivery_type': this.deliveryType,
          'cost': this.cost,
          'delivery_cost': this.deliveryType==='курьер'?this.courier_cost:0,
          'total_cost':  this.deliveryType==='курьер'?this.courier_cost+this.cost:this.cost,
          'items': items,
        }
        console.log(formData)
        await axios
            .post('/api/catalog/checkout/', formData)
            .then(() => {
              this.$store.state.isAuthenticated?
                  this.$router.push({name: 'account'}):
                  this.$router.push({name: 'catalog'})
              this.$toasted.success('Заказ оформлен', {icon: 'truck-fast'})
              this.$store.state.cart = []
              localStorage.setItem('cart', [])
            })
            .catch(error => {
              if (error.response) {
                this.errors = error.response.data
              }
            })

        this.$store.commit('SET_IS_LOADING', false)
      }
    },

    bindListener(mark) {
      this.mark = mark
      document.getElementById('btn_choose').addEventListener('click', this.chooseMark);
    },
    unbindListener() {
      this.mark = {}
      document.getElementById('btn_choose').removeEventListener('click', this.chooseMark);
    },

    chooseMark() {
      this.selectedMark = this.mark
      this.$toasted.show('Постамат выбран', {icon:'house'})
    },
    getAllPoints() {
      axios
          .get(`http://localhost:8080/pvzlist/v1/json?countryid=1&status=ACTIVE${'&fiasGuid=' + this.dadata_city.city_fias_id}`)
          .then(resp => {
            this.surfaces = resp.data.pvz
          })
          .catch(error => {
            console.log(error)
          })
    }

  },
  async mounted() {
    this.mask = new IMask(document.getElementById('phone'), {mask: '+7(000)000-00-00'});
  },
  validations: {
    email: {required, email,},
    firstname: {required,},
    lastname: {required,},
    phone: {required, minLength: minLength(16),},
    address_str: {required,}
  },


}
</script>

<style lang="scss" scoped>
.card {
  border: 2px solid rgba(0, 0, 0, 0.1);
  border-radius: 0.65rem;
}

/*Card Button CSS*/
.card-radio-btn {
  display: block;
}

.card-radio-btn .content_head {
  color: #333;
  text-align: left;
  font-size: 1.2rem;
  line-height: 30px;
  font-weight: 500;
}

.card-radio-btn .content_sub {
  color: #9e9e9e;
  text-align: right;
  font-size: 14px;
}

.card-input-element + .card {
  width: auto;
  margin-bottom: 10px;
  justify-content: center;
  color: var(--primary);
  border: 2px solid transparent;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 25px 0 rgba(0, 0, 0, 0.1);
}

.card-input-element + .card:hover {
  cursor: pointer;
}

.card-input-element:checked + .card {
  border: 2px solid $dark-color;
  transition: border 0.5s;
}

.card-input-element:checked + .card::after {
  content: "✔";
  color: rgba(0, 100, 0, 0.6);
  border: solid 2px;
  border-radius: 50%;
  width: 25px;
  height: 25px;
  position: absolute;
  right: 10px;
  top: 10px;
  font-style: normal;
  font-size: 1rem;
  font-weight: 900;
  line-height: 1.32;
  animation-duration: 0.5s;
}

.v-map__mapping {
  filter: saturate(130%);
}

.invalid_feedback {
  color: red;
  font-size: 15px;
}
</style>