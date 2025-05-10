import api from "@/plugins/axios/index.js";



export default {
  getCategory(params) {
    return api.get('category/all');
  },
  getProductCategory(category_id) {
    return api.get(`product/category/${category_id}`)
  }
}
