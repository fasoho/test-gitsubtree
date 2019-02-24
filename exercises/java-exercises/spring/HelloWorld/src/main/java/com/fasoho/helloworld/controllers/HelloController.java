package com.fasoho.helloworld.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * @project helloworld
 * @user jp
 * @date 2019-02-16
 */
@Controller
public class HelloController {
  @RequestMapping(value = "/", method = RequestMethod.GET)
  public String hello(@RequestParam(value="name", required=false, defaultValue="World") String name, Model model) {
    model.addAttribute("name", name);
    return "index";
  }
}