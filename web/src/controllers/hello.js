import { Controller } from "stimulus"

export default class extends Controller {
    static targets = ['name']
    connect() {
        this.nameTarget.value = 'BooFoo'
    }
    hello() {
        console.dir(this.nameTarget)
    }
}
