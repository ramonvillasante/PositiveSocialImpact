# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Welcome to PositiveSocialImpact! \n\n')
        self.response.write('PositiveSocialImpact is a web app to make positive impact action to sustainable development. \n') 
        self.response.write('This web app is based on the sustainable development research \n')
        self.response.write('and feedback of 80 user interviews integrated in this prototype https://invis.io/9874GSJS6. \n')
        self.response.write('We have a pitch deck https://goo.gl/yZ1eWT for the social enterprise planned when the first funding round could be achieved. \n')
        self.response.write('Check out this information and give us your feedback and collaboration ideas. Thank you! :) \n')
        self.response.write('This web is under development and will we updated every 1 or 2 weeks. \n')
        self.response.write('Last update: 1 Ago 2017 \n')
        
        
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
