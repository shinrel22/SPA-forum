<!--suppress ALL -->
<template>
  <div :id="name">
    <slot name="filters"></slot>
    <div class="row">
      <table :id="'mainbody-' + name" class="table table-striped table-bordered no-footer" role="grid" style="position: relative">
        <slot name="loading"></slot>
        <slot name="thead"></slot>
        <slot name="tbody"></slot>
      </table>
    </div>
    <div class="row">
      <div id="pagination">
        <div class="col-md-6" v-show="showEntries">
          <p class="m-t-30">Showing {{ 1 + (currentPage - 1) * perPage }} to {{ perPage * currentPage >
          totalRecords ? totalRecords : perPage * currentPage }} of {{
            totalRecords }} entries</p>
        </div>
        <div class="col-md-6" v-show="showPagination">
          <div class="dataTables_paginate paging_simple_numbers pull-right">
            <ul class="pagination">
              <li :class="currentPage <= 1 ? 'text-muted disabled' : ''" class="paginate_button"><a @click="first"><i
                :class="currentPage <= 1 ? 'text-muted' : ''"
                class="glyphicon glyphicon-fast-backward"></i></a></li>
              <li :class="currentPage <= 1 ? 'text-muted disabled' : ''" class="paginate_button"><a @click="previous"><i
                :class="currentPage <= 1 ? 'text-muted' : ''"
                class="glyphicon glyphicon-backward"></i></a>
              </li>
              <li style="cursor: pointer" v-for="index in (paginationButtons)" class="paginate_button"
                  :class="index === currentPage ? 'active' : ''"><a @click="change_page(index)">{{ index }}</a></li>
              <li :class="currentPage >= pages ? 'text-muted disabled' : ''" class="paginate_button" style="cursor: pointer">
                <a @click="next"><i
                  :class="currentPage >= pages ? 'text-muted' : ''"
                  class="glyphicon glyphicon-forward"></i></a></li>
              <li :class="currentPage >= pages ? 'text-muted disabled' : ''" class="paginate_button">
                <a @click="last"><i class="glyphicon glyphicon-fast-forward"
                                    :class="currentPage >= pages ? 'text-muted' : ''"></i></a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    props: {
      totalRecords: {type: Number, default: 0},
      currentPage: {type: Number, default: 1},
      perPage: {type: Number, default: 1},
      isLoading: {type: Boolean, default: false},
      showEntries: {type: Boolean, default: true},
      showPagination: {type: Boolean, default: true},
      showPerPage: {
        type: Boolean,
        default: true
      },
      name: {
        type: String,
        default () {
          return 'XoanTable'
        }
      }
    },
    data () {
      return {
        fakeCurrentPage: 1
      }
    },
    computed: {
      paginationButtons () {
        let currentPage = this.currentPage
        let pages = this.pages
        let result = []
        if (currentPage === 1) {
          for (let i = currentPage; i <= pages && i <= currentPage + 2; i++) {
            result.push(i)
          }
          return result
        }
        if (currentPage === pages) {
          for (let i = pages; i > 0 && i >= currentPage - 2; i--) {
            result.push(i)
            result.sort((a, b) => {
              return a - b
            })
          }
          return result
        }
        return [currentPage - 1, currentPage, currentPage + 1]
      },
      pages () {
        let result = this.totalRecords / this.perPage
        if (parseInt(result) < result) {
          result = parseInt(result)
          result++
        }
        return result
      }
    },
    methods: {
      change_page (page) {
        if (this.isLoading) return
        this.fakeCurrentPage = parseInt(page)
      },
      next () {
        if (this.isLoading) return
        if (this.fakeCurrentPage < this.pages) {
          this.fakeCurrentPage++
        }
      },
      previous () {
        if (this.isLoading) return
        if (this.fakeCurrentPage > 1) {
          this.fakeCurrentPage--
        }
      },
      last () {
        if (this.isLoading) return
        this.fakeCurrentPage = this.pages
      },
      first () {
        if (this.isLoading) return
        this.fakeCurrentPage = 1
      }
    },
    watch: {
      'fakeCurrentPage': function (value) {
        if (this.isLoading) return
        this.$emit('change_currentPage', value)
      },
      'currentPage': function (value) {
        this.fakeCurrentPage = this.currentPage
      }
    },
    beforeMount () {
    },
    mounted () {
      console.log('Xoan table mounted')
    }
  }
</script>
<style scoped>
  td {
    border: none !important;
  }
</style>
