<script>
  /*eslint-disable*/
  import VALIDATORS from '@/assets/constants/validators'
  /*eslint-enable*/
  export default {
    name: 'InputTag',
    props: {
      inputWidth: {type: Number, default: 150},
      inputClass: {
        type: String
      },
      tags: {
        type: Array,
        default: () => []
      },
      placeholder: {
        type: String,
        default: ''
      },
      onChange: {
        type: Function
      },
      readOnly: {
        type: Boolean,
        default: false
      },
      validate: {
        type: String,
        default: ''
      }
    },
    data () {
      return {
        newTag: ''
      }
    },
    methods: {
      focusNewTag () {
        if (this.readOnly) { return }
        this.$el.querySelector('.new-tag').focus()
      },
      addNew (tag) {
        if (tag && !this.tags.includes(tag) && this.validateIfNeeded(tag)) {
          this.tags.push(tag)
          this.tagChange()
        }
        this.newTag = ''
      },
      validateIfNeeded (tagValue) {
        if (this.validate === '' || this.validate === undefined) {
          return true
        } else if (Object.keys(VALIDATORS).indexOf(this.validate) > -1) {
          return VALIDATORS[this.validate].test(tagValue)
        }
        return true
      },
      remove (index) {
        this.tags.splice(index, 1)
        this.tagChange()
      },
      removeLastTag () {
        if (this.newTag) { return }
        this.tags.pop()
        this.tagChange()
      },
      getPlaceholder () {
        if (!this.tags.length) {
          return this.placeholder
        }
        return ''
      },
      tagChange () {
        if (this.onChange) {
          // avoid passing the observer
          this.onChange(JSON.parse(JSON.stringify(this.tags)))
        }
      }
    }
  }
</script>

<template>

  <div @click="focusNewTag()" v-bind:class="{'read-only': readOnly}" class="vue-input-tag-wrapper">
    <span v-for="(tag, index) in tags" class="input-tag">
      <span>{{ tag }}</span>
      <a v-if="!readOnly" @click.prevent.stop="remove(index)" class="remove"></a>
    </span>
    <input v-if="!readOnly" v-bind:placeholder="getPlaceholder()" type="text" v-model="newTag"
           v-on:keydown.delete.stop="removeLastTag()" v-on:keydown.enter.prevent.stop="addNew(newTag)"
           :style="{'width': inputWidth + 'px'}"
           :class="inputClass" class="new-tag"/>
  </div>

</template>

<style>

  .vue-input-tag-wrapper {
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    overflow: hidden;
    padding-left: 12px;
    padding-top: 4px;
    cursor: text;
    text-align: left;
    -webkit-appearance: textfield
  }

  .vue-input-tag-wrapper .input-tag {
    background-color: #cde69c;
    border-radius: 2px;
    border: 1px solid #a5d24a;
    color: #638421;
    display: inline-block;
    font-size: 13px;
    font-weight: 400;
    margin-bottom: 4px;
    margin-right: 4px;
    padding: 3px
  }

  .vue-input-tag-wrapper .input-tag .remove {
    cursor: pointer;
    font-weight: bold;
    color: #638421
  }

  .vue-input-tag-wrapper .input-tag .remove:hover {
    text-decoration: none
  }

  .vue-input-tag-wrapper .input-tag .remove::before {
    content: " x"
  }

  .vue-input-tag-wrapper .new-tag {
    background: transparent;
    border: 0;
    color: #777;
    font-size: 13px;
    font-weight: 400;
    margin-bottom: 6px;
    margin-top: 1px;
    outline: none;
    padding: 4px;
    padding-left: 0;
    width: 80px
  }

  .vue-input-tag-wrapper.read-only {
    cursor: default
  }

</style>
