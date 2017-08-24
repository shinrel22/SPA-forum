import $ from './NodeList.js'

export default {
  props: {
    content: {type: String},
    effect: {type: String, default: 'fade'},
    header: {type: Boolean, default: true},
    placement: {type: String, default: 'top'},
    title: {type: String},
    trigger: {type: String},
    triggerByModel: {type: Boolean, default: false},
    triggerByFunction: {type: Boolean, default: false},
    func: {type: Function},
    model: {type: Boolean}
  },
  data () {
    return {
      top: 0,
      left: 0,
      show: false
    }
  },
  computed: {
    events () {
      return {contextmenu: ['contextmenu'], hover: ['mouseleave', 'mouseenter'], focus: ['blur', 'focus']}[this.trigger] || ['click']
    }
  },
  methods: {
    beforeEnter () {
      this.position()
      setTimeout(() => this.position(), 30)
    },
    position () {
      this.$nextTick(() => {
        let popover = this.$refs.popover
        let trigger = this.$refs.trigger.children[0]
        switch (this.placement) {
          case 'top' :
            this.left = trigger.offsetLeft - popover.offsetWidth / 2 + trigger.offsetWidth / 2
            this.top = trigger.offsetTop - popover.offsetHeight
            break
          case 'left':
            this.left = trigger.offsetLeft - popover.offsetWidth
            this.top = trigger.offsetTop + trigger.offsetHeight / 2 - popover.offsetHeight / 2
            break
          case 'right':
            this.left = trigger.offsetLeft + trigger.offsetWidth
            this.top = trigger.offsetTop + trigger.offsetHeight / 2 - popover.offsetHeight / 2
            break
          case 'bottom':
            this.left = trigger.offsetLeft - popover.offsetWidth / 2 + trigger.offsetWidth / 2
            this.top = trigger.offsetTop + trigger.offsetHeight
            break
          default:
            console.warn('Wrong placement prop')
        }
        popover.style.top = this.top + 'px'
        popover.style.left = this.left + 'px'
      })
    },
    toggle (e) {
      if (this.triggerByModel) {
        this.show = this.model
        return
      }
      if (e && this.trigger === 'contextmenu') e.preventDefault()
      this.show = !this.show
      if (this.show) this.beforeEnter()
    }
  },
  mounted () {
    let trigger = this.$refs.trigger.children[0]
    if (!trigger) return console.error('Could not find trigger v-el in your component that uses popoverMixin.')

    if (this.trigger === 'focus' && !~trigger.tabIndex) {
      trigger = $('a,input,select,textarea,button', trigger)
      if (!trigger.length) { return }
    }
    if (this.triggerByModel) {
      this.toggle()
      return
    }
    this.events.forEach(event => {
      $(trigger).on(event, this.toggle)
    })
  },
  beforeDestroy () {
    if (this._trigger) $(this._trigger).off()
  }
}
