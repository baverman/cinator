import { Controller } from "stimulus"

export default class extends Controller {
    static targets = ['name']
    hello() {
        console.dir(this.nameTarget)
    }
}
