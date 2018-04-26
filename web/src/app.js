import { Application } from "stimulus"

export const application = Application.start()

import Hello from "./controllers/hello"
application.register("hello", Hello)
